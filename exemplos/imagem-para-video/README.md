# Exemplo: imagem pronta → vídeo de 15 s (2026-10-13)

Arte de anúncio do INEMA.CLUB ("Aprenda IA na prática", 1:1) animada pelo `agnes-video-2.5-flash`.

| | |
|---|---|
| Entrada | `fonte.jpg` (cópia reduzida; a original era PNG 1254×1254) |
| Saída | vídeo de 15,0 s, 720×720, sem áudio — no guia: [`guia/assets/exemplo-imagem-video-15s.mp4`](../../guia/assets/exemplo-imagem-video-15s.mp4) |
| Folha de contato | `contato.jpg` (um quadro a cada 2 s) |
| Modelo | `agnes-video-2.5-flash`, `mode:"keyframe"`, `seconds:"8"`, `aspect_ratio:"1:1"`, `size:"720P"` |
| Custo | US$ 0 |
| Tempo | ~25 min por clipe na fila; o 2º pegou 3× `503 video_queue_full` antes de entrar |

## Como foi feito

1. **Clipe 1** — `first_frame` = `last_frame` = a imagem. Prompt: ela sorri, acena com a cabeça, ri e volta à pose.
2. **Clipe 2** — só `first_frame` = a imagem. Prompt: sorri, pisca, inclina a cabeça, push-in lento.
3. Emenda 1 → 2 (o 1 termina exatamente onde o 2 começa: na imagem) e corta em 15 s.

Os dois prompts terminam com: *"All printed text, the phone screen, the logo and the blue badge stay
perfectly still, sharp and unchanged."* Resultado: o texto da arte não deformou em nenhum quadro.

## Refazer com outra imagem

```bash
python3 imagem_video.py arte.png --segundos 15 --proporcao 1:1 --saida ~/projetos/output/videos-agnes/minha-arte
```
