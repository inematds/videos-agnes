"""Imagem pronta (arte, anúncio, foto) -> vídeo de N segundos com o agnes-video-2.5-flash.

O 2.5-flash faz no máximo 12 s por clipe. Para passar disso, gera vários clipes que
COMEÇAM E TERMINAM na própria imagem (first_frame = last_frame = imagem), o que deixa
a emenda invisível; o último clipe termina livre. Depois corta na duração pedida.

Uso:
  python3 imagem_video.py arte.png --segundos 15 --saida ~/projetos/output/videos-agnes/x \
      [--proporcao 1:1] [--prompt "o que se mexe na cena, em inglês"]

Exemplo real (2026-10-13): anúncio INEMA.CLUB 1:1 -> 15 s, 2 clipes de 8 s, texto da arte
intacto do começo ao fim. Ver exemplos/imagem-para-video/.
"""
import argparse, json, math, os, subprocess, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

FIXO = ('All printed text, logos, badges and screens stay perfectly still, sharp and unchanged. '
        'Photorealistic, natural light.')
PADRAO = ('The person in the image smiles at the camera, blinks naturally and moves subtly; '
          'hair moves gently. Very slow cinematic push-in.')


def clipe(dest, img_uri, prompt, segundos, proporcao, volta):
    if os.path.exists(dest):
        print(f'  [{os.path.basename(dest)}] já existe', flush=True)
        return dest
    body = {'model': P.VIDEO_MODEL, 'prompt': f'Advertising video. {prompt} {FIXO}',
            'mode': 'keyframe', 'seconds': str(segundos), 'n': 1, 'size': '720P',
            'aspect_ratio': proporcao, 'first_frame': img_uri}
    if volta:
        body['last_frame'] = img_uri
    vid = None
    for t in range(1, 9):
        try:
            d = P._post(P.VID_API, body, timeout=300)
            vid = d.get('id') or d.get('task_id') or d.get('video_id')
            break
        except urllib.error.HTTPError as e:
            print(f'    HTTP {e.code}: {e.read()[:120].decode(errors="ignore")}', flush=True)
            time.sleep(70 if e.code == 429 else 30 * t)   # 503 video_queue_full é comum
        except Exception as e:
            print(f'    erro: {str(e)[:80]}', flush=True)
            time.sleep(40)
    if not vid:
        return None
    print(f'  [{os.path.basename(dest)}] job {vid}', flush=True)
    t0 = time.time()
    while time.time() - t0 < P.ESPERA_VIDEO:
        try:
            st = P._get(P.VID_GET + vid)
            if st.get('status') == 'completed':
                u = (st.get('video_url') or st.get('url') or (st.get('metadata') or {}).get('url'))
                open(dest, 'wb').write(urllib.request.urlopen(u, timeout=300).read())
                print(f'  [{os.path.basename(dest)}] {P.dur(dest):.1f}s', flush=True)
                return dest
            if st.get('status') == 'failed':
                print(f'  ❌ falhou: {json.dumps(st)[:200]}', flush=True)
                return None
        except Exception:
            pass
        time.sleep(15)
    print(f'  ❌ timeout (video_id={vid}) — rode de novo', flush=True)
    return None


def main():
    a = argparse.ArgumentParser()
    a.add_argument('imagem')
    a.add_argument('--segundos', type=float, default=15)
    a.add_argument('--saida', required=True)
    a.add_argument('--proporcao', default='1:1', help='16:9, 1:1, 9:16, 4:3, 3:4, 21:9')
    a.add_argument('--prompt', default=PADRAO)
    o = a.parse_args()
    os.makedirs(o.saida, exist_ok=True)
    n = max(1, math.ceil(o.segundos / 12))
    seg = max(4, min(12, math.ceil(o.segundos / n)))
    uri = P.keyframe(o.imagem)
    print(f'>> {n} clipe(s) de {seg}s ({P.VIDEO_MODEL}, {o.proporcao})', flush=True)
    partes = []
    for i in range(n):
        # todos voltam à imagem, menos o último: emenda invisível
        c = clipe(f'{o.saida}/clipe-{i+1:02d}.mp4', uri, o.prompt, seg, o.proporcao, volta=i < n - 1)
        if not c:
            sys.exit(f'❌ clipe {i+1} não saiu')
        partes.append(c)
    final = f'{o.saida}/video-{int(o.segundos)}s.mp4'
    ent = sum((['-i', p] for p in partes), [])
    filtro = ''.join(f'[{i}:v]setsar=1,fps=24[v{i}];' for i in range(n)) + \
        ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1[v]'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', *ent, '-filter_complex', filtro, '-map', '[v]',
                    '-t', str(o.segundos), '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p',
                    '-movflags', '+faststart', final], check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', final, '-vf', 'fps=1/2,scale=360:-1,tile=4x2',
                    '-frames:v', '1', f'{o.saida}/contato.jpg'], check=True)
    print(f'>> {final} · {P.dur(final):.1f}s · folha {o.saida}/contato.jpg (conferir o texto da arte)')


if __name__ == '__main__':
    main()
