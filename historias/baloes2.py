# "A Corrida dos Balões: A Grande Tempestade" — CONTINUAÇÃO de baloes.py
# Reusa o trio (Laura, Miguel, Ana) + Lumi. Novo desafio: uma tempestade e ajudar outro balão.

TITULO = 'A Corrida dos Balões: A Grande Tempestade'
LEGENDA = ('A Corrida dos Baloes: A Grande Tempestade (continuacao)\n'
           'imagens agnes-image-2.1-flash · video keyframes · narracao bella local. Custo US$ 0.')
VOZ = 'bella'

TRIO = ('Laura, a girl with brown braided hair; Miguel, a boy with black curly hair; Ana, a girl with '
        'blonde hair. Three children about nine years old')
LUMI = ('Lumi, a small magical glowing fairy guide with sparkling translucent wings, a warm smile, '
        'a trail of golden light')
STYLE = ('Pixar-style 3D animated feature film render, bright fantasy sky world, soft cinematic lighting, '
         'colorful magical atmosphere, restrained natural saturation')

ANCORAS = []   # reusadas do filme 1 (anc-trio, anc-lumi)

CENAS = [
    ('cena-01-a', f'{TRIO} and {LUMI} starting a new balloon race in a bright fantasy sky, cheerful and confident.',
     ['anc-trio', 'anc-lumi']),
    ('cena-01-b', 'Dark storm clouds gathering fast over the Valley of Clouds, lightning, ominous, wide shot.', []),
    ('cena-02-a', f'{TRIO} in their balloons caught in the storm, wind and rain, holding on tight, dramatic.',
     ['anc-trio']),
    ('cena-02-b', 'Another child alone in a small torn balloon losing altitude in the storm, in danger, calling for help.',
     []),
    ('cena-03-a', f'{TRIO} deciding to abandon the race to rescue the stranger, brave and kind.', ['anc-trio']),
    ('cena-03-b', f'{LUMI} creating a golden protective bubble of light around all the balloons against the storm.',
     ['anc-lumi']),
    ('cena-04-a', f'{TRIO} pulling the lost child safely into their balloon, teamwork, relief.', ['anc-trio']),
    ('cena-04-b', 'The storm clearing to reveal a brilliant double rainbow, calm bright sky, hopeful.', []),
    ('cena-05-a', f'{TRIO}, {LUMI} and the rescued new friend celebrating together in the sky, joyful.',
     ['anc-trio', 'anc-lumi']),
    ('cena-05-b', f'All the balloons flying home together at golden hour, a bigger group of friends now, warm ending.',
     ['anc-trio', 'anc-lumi']),
]

NARRACAO = {
    1: 'Os amigos começaram uma nova Corrida dos Balões, animados. Mas, no meio do caminho, nuvens escuras '
       'se formaram depressa sobre o Vale das Nuvens. Era uma grande tempestade!',
    2: 'O vento e a chuva balançavam os balões. De repente, eles viram outra criança sozinha, presa num balão '
       'rasgado, perdendo altura e pedindo socorro.',
    3: 'Sem pensar duas vezes, o trio decidiu abandonar a corrida para salvar o desconhecido. Lumi criou uma '
       'bolha dourada de luz para proteger todos da tempestade.',
    4: 'Com muito cuidado, eles puxaram a criança perdida para dentro do balão. Nesse instante, a tempestade '
       'passou e um lindo arco-íris duplo surgiu no céu.',
    5: 'Todos comemoraram juntos. A verdadeira vitória, disse Lumi, é ajudar quem precisa. E voltaram para casa '
       'com um novo amigo, formando um grupo ainda maior.',
}

MOVIMENTO = {
    1: 'the friends start the new race confidently, then dark storm clouds gather fast, lightning',
    2: 'the balloons rock in the wind and rain, then they spot a child alone in a torn balloon in danger',
    3: 'the trio bravely turn to rescue, then Lumi wraps the balloons in a golden protective bubble',
    4: 'they pull the lost child to safety, then the storm clears to a brilliant double rainbow',
    5: 'everyone celebrates in the sky, then all the balloons fly home together at golden hour',
}
