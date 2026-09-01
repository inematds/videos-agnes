# "Wobbly e o Robô Perdido" — CONTINUAÇÃO de wobbly.py
# Reusa os personagens do 1o filme (âncoras semeadas de output/wobbly) -> ANCORAS vazio.
# Mesmo tom slapstick.

TITULO = 'Wobbly e o Robô Perdido'
LEGENDA = ('Wobbly e o Robo Perdido (continuacao)\n'
           'imagens agnes-image-2.1-flash · video keyframes · narracao bella local. Custo US$ 0.')
VOZ = 'bella'

WOBBLY = ('Wobbly, a small floppy yellow rag-doll character with a round head, big cheerful eyes, '
          'thin wobbly arms and legs, clumsy and goofy')
BOB = ("Bob, Wobbly's friend, a small blue rag-doll character with a round head, a friendly grin, stitched seams")
ROBO = 'a small lost broken robot with one wheel, a cracked screen face, sparks, cute and sad'
STYLE = ('Pixar-style 3D animated feature film render, bright colorful playful world, soft cinematic '
         'lighting, warm saturated colors, comedic')

ANCORAS = []   # reusadas do filme 1 (anc-wobbly, anc-bob) — semeadas no estado.json

CENAS = [
    ('cena-01-a', f'{WOBBLY} and {BOB} bored at home surrounded by their treasure, wanting a new adventure.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-01-b', f'{WOBBLY} tripping over {ROBO}, a small broken robot lying in an alley of the colorful city, '
                  f'surprised.', ['anc-wobbly']),
    ('cena-02-a', f'{WOBBLY} and {BOB} looking at the sad broken robot, deciding to fix it, kind.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-02-b', f'{WOBBLY} comically trying to repair the robot with a giant wrench, sparks flying everywhere.',
     ['anc-wobbly']),
    ('cena-03-a', f'The little robot lighting up and beeping happily, fixed, {WOBBLY} and {BOB} cheering.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-03-b', f'{WOBBLY}, {BOB} and the robot riding a wobbly homemade cart down a hill in the city, chaotic fun.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-04-a', f'The three crashing softly into a pile of pillows at the bottom, laughing, dust cloud, comic.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-04-b', f'{WOBBLY}, {BOB} and the happy little robot together at sunset, new friends, warm ending.',
     ['anc-wobbly', 'anc-bob']),
]

NARRACAO = {
    1: 'Depois da grande aventura, Wobbly e Bob estavam ricos, mas entediados. Queriam uma nova aventura! '
       'Foi quando Wobbly, andando pela cidade, tropeçou em uma coisa estranha no beco.',
    2: 'Era um pequeno robô, quebrado e tristinho. Vamos consertar ele! disse Wobbly. Então pegou uma chave '
       'enorme e começou a mexer, com faíscas voando pra todo lado.',
    3: 'De repente, o robozinho acendeu e apitou de alegria! Estava consertado! Para comemorar, os três subiram '
       'num carrinho maluco e desceram a ladeira em alta velocidade.',
    4: 'No fim, caíram numa pilha de almofadas, rindo sem parar. E assim Wobbly e Bob ganharam um novo amigo, '
       'o pequeno robô, e mais um dia maluco terminou feliz na cidade de Wobbly.',
}

MOVIMENTO = {
    1: 'Wobbly and Bob sit bored, then Wobbly trips over the little broken robot in the alley',
    2: 'the two look at the sad robot, then Wobbly comically fixes it with a giant wrench, sparks flying',
    3: 'the robot lights up beeping happily, then the three ride a wobbly cart chaotically down a hill',
    4: 'they crash softly into pillows laughing, then sit together at sunset as new friends',
}
