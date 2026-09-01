# Modelos da API Agnes — medições brutas

Tudo aqui foi **medido na API** (`apihub.agnes-ai.com`) com a chave desta assinatura, não copiado de
documentação. Cada linha traz a data. A API muda: **re-medir antes de confiar em número antigo.**

Resumo e decisões de produção ficam no [README](README.md). Aqui fica o detalhe.

---

## 1. Listagem `/v1/models` — oscila

| Data | Nº de modelos | Observação |
|---|---|---|
| 2026-08-31 | 11 | incluía `agnes-video-2.5`, `agnes-2.5-pro`, `-pro-beta`, `-pro-alpha` |
| 2026-09-01 | 7 | os 4 acima **sumiram** da lista |

Listagem de 2026-09-01: `agnes-2.0-flash`, `agnes-2.5-flash`, `agnes-image-2.0-flash`,
`agnes-image-2.1-flash`, `agnes-image-2.5-flash`, `agnes-video-2.5-flash`, `agnes-video-v2.0`.

O campo `created` é **falso** (`1626777600` para todos) — não serve para saber data de lançamento.
`agnes-image-2.5-flash` vem com `supported_endpoint_types: []` (vazio) e **mesmo assim funciona**.

`agnes-video-2.5` (não-flash), chamado direto:
`503 — No available channel for model agnes-video-2.5 under group TokenPlan (distributor)`.

---

## 2. Vídeo

### 2.1 `agnes-video-v2.0` (em uso no pipeline)

Campos: `num_frames` (8n+1), `frame_rate`, `width`/`height`, `seed`, `negative_prompt`,
`extra_body.image` + `extra_body.mode` (`keyframes` | `ti2vid`). Polling: `GET /agnesapi?video_id=`.

Teto de `num_frames` por resolução (a própria API devolve a tabela no 400) — medido 2026-08-31:

| Resolução | Máx `num_frames` | @24fps |
|---|---|---|
| 480p | 961 | 40,0s |
| 720p | 481 | 20,0s |
| 1080p | 241 | 10,0s |

Proporção não altera o teto. Fora do 8n+1 → 400 `num_frames must equal 8 * n + 1`.

### 2.2 `agnes-video-2.5-flash` — schema incompatível (medido 2026-09-01)

**Campos proibidos** (400 `forbidden field` / `not an allowed request field`):
`num_frames`, `frame_rate`, `width`, `height`, `quality`, `resolution`.
Campo desconhecido → 400 `<campo> is not an allowed request field` (o 2.0 descartava em silêncio).

| Campo | Valor aceito | Erro que revelou |
|---|---|---|
| `mode` (obrigatório) | `text`, `reference`, `keyframe` | `mode is required` / `invalid mode` |
| `seconds` | **string** `"4"`–`"12"` | `seconds must be in [4, 12]`; número → `invalid_json` (espera string) |
| `aspect_ratio` | `21:9` `16:9` `4:3` `1:1` `3:4` `9:16` | `aspect_ratio must be one of ...` |
| `size` | erro cita `720P`,`960P`,`2K` — **mas esta conta só aceita `720P`** | pedir `2K` → 400 `size must be 720P` |
| `images` (modo `reference`) | até **5**; também aceita `audios` e `videos` | `images length must not exceed 5` |
| `first_frame` / `last_frame` (modo `keyframe`) | — | `keyframe mode requires first_frame and/or last_frame` |

Nomes que **não** existem: `t2v`, `t2vid`, `text2video`, `txt2vid`, `i2v`, `ti2vid`, `keyframes`,
`frames`, `first_last`, `start_end`, `transition`, `image`.

**Polling muda:** `GET /v1/videos/<task_id>`. O `GET /agnesapi?video_id=<id>` do 2.0 devolve
**404 `task not found`** para tarefas 2.5.

Geração real (2026-09-01), `mode:"text"`, `seconds:"4"`, `aspect_ratio:"16:9"`:
`queued` → `completed` em **62s**, custo US$ 0, MP4 em `platform-outputs.agnes-ai.space`.
ffprobe: **1280x704, 24fps, 4,458s, 107 frames** — o tamanho **mente** igual ao 2.0 (16:9 pedido,
1280x704 entregue) e a duração real passa um pouco dos `seconds` pedidos.

**Rate limit:** 6 req/min, o mesmo do 2.0 — e **requisições inválidas (400) contam** para o limite.
Erro: `video generation rate limit exceeded: allows 6 requests per 1 minute(s)`.

---

## 3. Imagem — `2.0-flash` × `2.1-flash` × `2.5-flash` (medido 2026-09-01)

Os três estão **liberados** e respondem no mesmo `POST /v1/images/generations`, com o **mesmo
schema**. Resposta idêntica nos três: `{data:[{url, b64_json, revised_prompt}], created, task_id}`.

| Teste | 2.0-flash | 2.1-flash | 2.5-flash |
|---|---|---|---|
| `size:"1K"` text2img | ✅ 1024×1024 | ✅ 1024×1024 | ✅ 1024×1024 |
| `size:"1K"` + `ratio:"16:9"` | ✅ **1312×736** | ✅ **1312×736** | ✅ **1312×736** |
| `size:"1312x736"` (pixels) | ✅ 1312×736 | ✅ 1312×736 | ✅ 1312×736 |
| `seed:42` | 200, **ignorado** | 200, **ignorado** | 200, **ignorado** |
| img2img 1 ref + `ratio:"16:9"` | — | ✅ **1312×736** | ✅ **1312×736** |
| img2img **5 refs** | — | ⚠️ entregou **duas raposas** | ✅ **uma raposa**, cena limpa |

### ⚠️ Correção do que estava documentado

O README dizia "**`ratio` é IGNORADO em img2img** — volta 1024×1024". **Não reproduz mais**
(2026-09-01): `1K` + `ratio:16:9` **com referência** devolveu 1312×736 no 2.1 e no 2.5.
Ou a API mudou, ou a medição original tinha outra variável junto. O contorno (pixels explícitos em
`size`) continua correto e mais seguro — só não é mais obrigatório.

### 5 referências

O limite de "2 refs úteis, 5 destroem a imagem" foi medido no **2.1**. No teste de 2026-09-01 com
**5 cópias da mesma imagem**: o 2.1 duplicou o personagem (defeito clássico), o **2.5 não duplicou**.
⚠️ **Indício, não prova** — n=1, e 5 cópias iguais não é o caso real (5 vistas distintas do mesmo
personagem). Precisa de repetição antes de virar regra de produção.

### Instabilidade

Continua alta: na rodada de 2026-09-01, **4 de 6 primeiras chamadas falharam** com
`503 text image queue is full, please retry later` ou `500 internal error` — recuperadas com
backoff (até 4 retries). Retry com backoff **não é opcional**.

---

## 4. Cotas — o que é fato e o que não é

| Afirmação | Fonte | Status |
|---|---|---|
| **500 s/dia de vídeo no `agnes-video-v2.0`** | painel da conta (usuário, 2026-09-01) | ✅ visto no painel — a API não confirma |
| Cota diária do `agnes-video-2.5-flash` | — | 🔬 **em teste** (2026-09-01) |
| "200 s/dia" | terceiros | ⚠️ não confirmado aqui |
| "2.5 Flash grátis temporariamente em 720p" | doc de terceiro | ⚠️ plausível (aqui é US$ 0 e só 720P), "temporariamente" sem confirmação |
| "Video 2.5 lançado em 2026-08-27" | doc de terceiro | ⚠️ não verificável (o `created` da API é falso) |
| 1080p / 2K no 2.5 "na versão paga" | doc de terceiro | ❌ contradito nesta conta (`size must be 720P`) |
| Cota de **imagem** | — | ❓ nunca medida; só se vê saturação pela taxa de 503 |

**A API não expõe cota:** `/v1/rate_limits`, `/v1/limits`, `/v1/me` → 404; `/v1/models/<id>` →
`model_not_found`; `/v1/dashboard/billing/subscription` devolve placeholder
(`hard_limit_usd: 100000000`, `total_usage: 0`) igual para qualquer plano; não há headers
`X-RateLimit-*`. **O 429 é o único aviso de limite.**

---

## 5. Em aberto (nada disso está medido)

- Cota diária do 2.5-flash (em teste).
- Qualidade comparada 2.0 × 2.5-flash em vídeo (nenhum A/B ainda).
- Modo `reference` do vídeo 2.5 com `audios`/`videos` — aceito pelo validador, nunca executado.
- Modo `keyframe` do 2.5 (`first_frame`/`last_frame`) — validado, nunca renderizado.
- 5 refs distintas na imagem 2.5 (o teste foi com cópias iguais).
- Se `agnes-video-2.5` (não-flash) e os `agnes-2.5-pro*` voltam à listagem.
