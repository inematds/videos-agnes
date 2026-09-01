# Dependências do videos-agnes

De onde este projeto depende para ir de `historias/<nome>.py` até o MP4 narrado.
Levantado lendo `pipeline.py`, `rodar.py`, `revisao.py` e conferido nos logs de execução
(`~/projetos/output/videos-agnes/*.log`) em 2026-08-14.

## Mapa rápido

```
historias/<nome>.py
      │
      ├─ [1] âncoras ──┐
      ├─ [2] cenas ────┴─► Agnes AI  ·  apihub.agnes-ai.com  (imagem)
      ├─ [3] narração ───► inemavox  ·  localhost:8010       (TTS local)
      ├─ [4] clipes ─────► Agnes AI  ·  apihub.agnes-ai.com  (vídeo)
      ├─ [5] montagem ───► ffmpeg / ffprobe                  (binários locais)
      └─ [6] entrega ────► api.telegram.org                  (openpcbot)
```

Nenhuma etapa chama outra **skill**. Tudo é HTTP direto ou subprocess.
As skills irmãs entram só por decisão do agente — ver "Skills irmãs" no fim.

---

## 1. Serviços externos (rede)

### Agnes AI — `apihub.agnes-ai.com`

Gateway litellm sobre one-api. **Custo US$ 0**, sem créditos.

| Endpoint | Uso | Modelo |
|---|---|---|
| `POST /v1/images/generations` | âncoras e cenas | `agnes-image-2.1-flash` |
| `POST /v1/videos` | clipes keyframe A→B | `agnes-video-v2.0` (existe `agnes-video-2.5-flash`, não adotado) |
| `GET /agnesapi?video_id=` | polling do clipe | — |

- **Credencial:** `AGNES_API_KEY` lida de `~/projetos/agnes-nei/.env` (`pipeline.py:32`).
  Caminho **hardcoded** — se esse arquivo sumir, o pipeline quebra na importação.
- **Rate limit real:** **6 req/min** no vídeo → HTTP 429 (medido 2026-08-31; a API responde
  `allows 6 requests per 1 minute(s)`). Mesmo teto no `agnes-video-2.5-flash`. `rodar.py` pausa
  65s a cada 4 clipes — conservador, e continua válido.
- **Instabilidade medida:** ~34% de HTTP 503 na imagem; retry com backoff é obrigatório e já
  está embutido. Nos logs: 12 ocorrências de 503 recuperadas por retry, e uma rajada de 429
  no `montanha` (18 seguidas) — todas absorvidas.
- **Sem cota consultável.** `/v1/dashboard/billing/*` devolve valores de preenchimento;
  `/v1/rate_limits`, `/v1/limits`, `/v1/me` → 404; não há headers `X-RateLimit-*` (verificado
  2026-08-31). O único medidor de saturação é a taxa de 503, e o 429 é o único aviso de limite.
- **`agnes-video-2.5` listado mas sem canal nesta assinatura:** 503 `No available channel ...
  under group TokenPlan`. Aparecer em `/v1/models` ≠ estar liberado — testar antes de adotar.

### Telegram — `api.telegram.org`

Entrega do MP4 final (`enviar_telegram`, `pipeline.py:226`).

- **Credenciais:** `TELEGRAM_BOT_TOKEN` + `ALLOWED_CHAT_ID` (ou `CHAT_ID`) lidos de
  `~/projetos/openpcbotv2/.env` — outro caminho hardcoded.
- **Teto de 50 MB.** Acima disso a API recusa; `montar()` já avisa no print.
- É a **única etapa que publica para fora**. Falha aqui não invalida o filme, que fica em disco.

---

## 2. Serviços locais (precisam estar no ar)

### inemavox — `http://localhost:8010`

TTS da narração (`narrar`, `pipeline.py:145`). Engine `chatterbox`, voz default `bella`
(tom de storytelling), `lang: pt`.

- `POST /api/jobs/tts/upload` (multipart) → `GET /api/jobs/<id>` (polling, teto 15min)
  → `GET /api/jobs/<id>/audio`.
- **Bloqueante para o resto do pipeline:** a duração da fala define `num_frames` de cada
  clipe. Sem inemavox no ar a etapa 3 falha e as etapas 4–6 não têm como continuar corretas.

### ffmpeg / ffprobe (PATH)

- `ffprobe` — mede duração de cada clipe e wav (`dur`).
- `ffmpeg` — casa fala com clipe (`tpad`/`apad`, padding; **nunca corta fala**), concata via
  `-f concat`, saída H.264 crf 27 + AAC 128k com `+faststart`.

---

## 3. Arquivos de outros projetos

| Caminho | Para quê | Se sumir |
|---|---|---|
| `~/projetos/agnes-nei/.env` | `AGNES_API_KEY` | quebra no import de `pipeline.py` |
| `~/projetos/openpcbotv2/.env` | token e chat do Telegram | só a entrega falha |
| `~/projetos/timesmkt3/media/voice-refs/<voz>.wav` | áudio de referência da voz clonada | narração falha |

---

## 4. Python

**Só stdlib** — `base64`, `json`, `os`, `subprocess`, `time`, `urllib.request`, `urllib.error`,
`re`, `uuid`, `importlib`, `sys`. Sem `requirements.txt`, sem venv, sem pacote de terceiros.

---

## 5. Limites embutidos (não são bugs)

| Limite | Valor | Onde |
|---|---|---|
| Frames por clipe | ≤ 441 (18,4s @24fps), regra 8n+1 | `frames_para` |
| Polling de clipe | 45 min (`ESPERA_VIDEO`) | `gerar_video` |
| Polling de TTS | 15 min | `narrar` |
| Referências por imagem | 2 úteis, 10 MB cada | regra da API |
| Vídeo no Telegram | 50 MB | API do Telegram |
| `seed` na imagem | **não existe** — daí a deriva de identidade | regra da API |

---

## 6. Falha silenciosa — corrigida em 2026-08-14

O clipe podia ficar `in_progress` além do teto de polling; `gerar_video` retornava `None`
**sem imprimir nada**, e `montar()` seguia pulando o clipe ausente. O filme saía curto e ia
para o Telegram como se estivesse inteiro.

Aconteceu de verdade com o `luna2` (`luna2.log`): narração de 49s em 4 cenas, só o clipe-01
gerou, `>> filme-luna2: 13.4s` e `✅ enviado`. Foi o único caso nos logs — as outras 5
histórias (`baloes`, `luna`, `montanha`, `wobbly`, `wobbly2`) fecharam com todos os clipes.

**O que mudou:**

- `montar()` confere os `n_cenas` clipes antes de qualquer coisa e **aborta** listando as
  cenas que faltam, sem sobrescrever um filme anterior. `parcial=True` monta assim mesmo,
  só para inspeção manual.
- `rodar.py` sai com **código 1** e não envia nada quando a montagem aborta.
- `gerar_video` imprime `❌` explícito nos quatro caminhos de falha (job recusado, completou
  sem URL, `failed`, timeout) — o timeout mostra o `video_id` para rastrear.
- Teto de polling do vídeo subiu de 30 → 45 min (`ESPERA_VIDEO`).

O pipeline é idempotente: rodar de novo retoma só o que falta.

---

## 7. Skills irmãs — invocar direto

O pipeline não depende de skill nenhuma, mas o **agente** deve chamar direto (ferramenta
Skill) nestes casos, em vez de descrever ou reimplementar:

| Situação | Skill |
|---|---|
| Assunto/história crua, sem cenas fatiadas | `roteiro` |
| Regerar uma cena torta, avulsa | `imagens-agnes` |
| Pediu decupagem, câmera, ritmo, ou escolher provedor | `videoanima` |
| Movimento em foto sem gerador de vídeo IA | `pixflow-motion` |

**Uso real nos logs:** as sessões mostram `python3 rodar.py <nome>` centenas de vezes
(exemplo, montanha, alien, xbox, diabrotic…) e a skill `videos-agnes` invocada pela
ferramenta Skill **uma única vez** — e a partir de outro projeto. Na prática o caminho é
sempre o CLI direto; a tabela acima existe para os casos em que ele não basta.
