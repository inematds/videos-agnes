# "A Corrida dos Balões Mágicos"
# 4 personagens: Laura, Miguel, Ana (crianças) + Lumi (guia mágica).
# Como o teto é 2 refs, uso âncora de GRUPO (o trio = 1 ref) + Lumi.
# Fantasia aérea: balões gigantes, 5 estrelas, Vale das Nuvens.

TITULO = 'A Corrida dos Balões Mágicos'
LEGENDA = ('A Corrida dos Baloes Magicos\n'
           '13 cenas · imagens agnes-image-2.1-flash · video keyframes agnes-video-v2.0 · '
           'narracao bella local. Custo US$ 0.')
VOZ = 'bella'

TRIO = ('Laura, a girl with brown braided hair; Miguel, a boy with black curly hair; Ana, a girl with '
        'blonde hair. Three children about nine years old')
LUMI = ('Lumi, a small magical glowing fairy guide with sparkling translucent wings, a warm smile, '
        'a trail of golden light')
STYLE = ('Pixar-style 3D animated feature film render, bright fantasy sky world, soft cinematic lighting, '
         'colorful magical atmosphere, restrained natural saturation')

ANCORAS = [
    ('anc-trio', f'Character reference sheet: {TRIO}, standing together side by side in a town square, '
                 f'three-quarter view, full body. Plain soft background.', None),
    ('anc-lumi', f'Character reference of {LUMI}, hovering in the air, three-quarter view, full body.', 'anc-trio'),
]

CENAS = [
    ('cena-01-a', f'{TRIO} meeting as best friends in a colorful town square on a Saturday morning, cheerful.',
     ['anc-trio']),
    ('cena-01-b', f'{LUMI} waiting for them in the square with a surprise smile, sparkles around her.', ['anc-lumi']),
    ('cena-02-a', f'{LUMI} snapping her fingers as four giant magical hot-air balloons, each a different bright color, '
                  f'appear over the square, wondrous.', ['anc-lumi']),
    ('cena-02-b', f'{TRIO} and {LUMI} boarding the colorful balloons, excited, about to start the adventure.',
     ['anc-trio', 'anc-lumi']),
    ('cena-03-a', 'Four giant colorful magical balloons floating up into a bright fantasy sky over a Valley of Clouds, '
                  'wide shot, adventurous.', []),
    ('cena-03-b', f'The first magic star glowing at the top of a rainbow, {TRIO} in their balloons reaching for it.',
     ['anc-trio']),
    ('cena-04-a', 'A magic star hidden inside a big fluffy cloud, soft glow, whimsical.', []),
    ('cena-04-b', 'A magic star shining near a brilliant sparkling waterfall in the sky, colorful mist.', []),
    ('cena-05-a', 'A magic star on a floating island full of colorful flowers in the sky, beautiful.', []),
    ('cena-05-b', f'A strong wind sweeping the four balloons in different directions, {TRIO} holding on, dramatic.',
     ['anc-trio']),
    ('cena-06-a', f'{TRIO} working together against the wind: one reading a magic map, one tying a glowing rope '
                  f'between the balloons, while {LUMI} creates a golden calming light.', ['anc-trio', 'anc-lumi']),
    ('cena-06-b', 'The fifth magic star hidden inside a great golden balloon, glowing brightly, discovery.', []),
    ('cena-07-a', 'All five magic stars shining together and coloring the whole sky with a beautiful rainbow, '
                  'triumphant, wide shot.', []),
    ('cena-07-b', f'{TRIO} and {LUMI} celebrating together with balloon-shaped medals, happy, golden light, '
                  f'teamwork, ending.', ['anc-trio', 'anc-lumi']),
]

NARRACAO = {
    1: 'Era uma vez três grandes amigos: Laura, Miguel e Ana. Em uma manhã de sábado, eles encontraram Lumi '
       'esperando por eles na praça da cidade. Tenho uma surpresa! disse Lumi sorrindo.',
    2: 'Com um estalar de dedos, apareceram quatro balões mágicos gigantes, cada um de uma cor diferente. '
       'Os quatro embarcaram em seus balões e começaram a aventura.',
    3: 'Hoje acontecerá a Grande Corrida dos Balões! Mas, para vencer, precisamos encontrar cinco estrelas '
       'mágicas escondidas pelo Vale das Nuvens. A primeira estrela estava no topo de um arco-íris.',
    4: 'A segunda estava escondida dentro de uma nuvem fofinha. A terceira foi encontrada perto de uma '
       'cachoeira brilhante.',
    5: 'A quarta estava em uma ilha flutuante cheia de flores coloridas. Quando faltava apenas uma estrela, '
       'um vento muito forte começou a soprar. Os balões foram levados para direções diferentes.',
    6: 'Não desistam! gritou Laura. Miguel usou um mapa mágico para encontrar o caminho. Ana amarrou uma corda '
       'brilhante entre os balões para que ninguém se perdesse. Lumi criou uma luz dourada que acalmou o vento. '
       'Logo encontraram a quinta estrela, escondida dentro de um grande balão dourado.',
    7: 'Assim que a tocaram, todas as estrelas começaram a brilhar e coloriram o céu com um lindo arco-íris. '
       'Eles venceram a corrida! Como prêmio, receberam uma medalha em forma de balão. A verdadeira vitória não '
       'foi chegar primeiro, disse Lumi, mas trabalhar em equipe. Os quatro voltaram para casa felizes.',
}

MOVIMENTO = {
    1: 'the three friends meet cheerfully in the square, then Lumi appears with a surprise smile and sparkles',
    2: 'Lumi snaps her fingers and four giant balloons appear, then the friends board them excited',
    3: 'the balloons float up into the fantasy sky, then reach for the first star atop a rainbow',
    4: 'a star glows inside a fluffy cloud, then another shines near a sparkling sky waterfall',
    5: 'a star on a floating flower island, then a strong wind sweeps the balloons apart, the kids holding on',
    6: 'the friends work together with map, rope and golden light, then find the fifth star in a golden balloon',
    7: 'all five stars shine and paint the sky with a rainbow, then everyone celebrates with balloon medals',
}
