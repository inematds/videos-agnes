"""Semeia o estado.json de uma CONTINUAÇÃO com as âncoras (base64) do filme original,
para os personagens serem os mesmos. Uso: python3 seed_ancoras.py <original> <sequel>"""
import base64, json, os, sys

BASE = '/home/nmaldaner/projetos/output/videos-agnes'
orig, seq = sys.argv[1], sys.argv[2]
od, sd = f'{BASE}/{orig}', f'{BASE}/{seq}'
os.makedirs(sd, exist_ok=True)
os.makedirs(f'{sd}/video', exist_ok=True)
os.makedirs(f'{sd}/narracao', exist_ok=True)

est = f'{sd}/estado.json'
S = json.load(open(est)) if os.path.exists(est) else {'urls': {}, 'dur': {}}
n = 0
for f in os.listdir(od):
    if f.startswith('anc-') and f.endswith('.png'):
        aid = f[:-4]
        S['urls'][aid] = 'data:image/png;base64,' + base64.b64encode(open(f'{od}/{f}', 'rb').read()).decode()
        n += 1
json.dump(S, open(est, 'w'), indent=2)
print(f'{seq}: {n} âncoras semeadas de {orig} -> {list(S["urls"].keys())}')
