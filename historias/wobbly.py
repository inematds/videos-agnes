# "A Grande Aventura de Wobbly na Cidade Maluca"
# Personagens (design inventado — o texto só diz "bonequinho amarelo meio molenga"):
#   Wobbly: boneco de pano amarelo, molenga, atrapalhado. Bob: amigo, boneco azul.
# Comédia slapstick — muita queda/batida. O humor vai na imagem + narração.

TITULO = 'A Grande Aventura de Wobbly na Cidade Maluca'
LEGENDA = ('A Grande Aventura de Wobbly na Cidade Maluca\n'
           '11 cenas · imagens agnes-image-2.1-flash · video keyframes agnes-video-v2.0 · '
           'narracao bella local. Custo US$ 0.')
VOZ = 'bella'

WOBBLY = ('Wobbly, a small floppy yellow rag-doll character with a round head, big cheerful eyes, '
          'thin wobbly arms and legs, clumsy and goofy')
BOB = ("Bob, Wobbly's friend, a small blue rag-doll character with a round head, a friendly grin, "
       'stitched seams')
STYLE = ('Pixar-style 3D animated feature film render, bright colorful playful world, soft cinematic '
         'lighting, warm saturated colors, comedic')

ANCORAS = [
    ('anc-wobbly', f'Character reference of {WOBBLY}, standing in a colorful cartoon city, three-quarter view, '
                   f'full body. Plain soft background.', None),
    ('anc-bob', f'Character reference of {BOB}, standing in a colorful cartoon city, three-quarter view, '
                f'full body.', 'anc-wobbly'),
]

CENAS = [
    ('cena-01-a', f'{WOBBLY} waking up happily in a small colorful bedroom on a sunny morning, arms up, joyful.',
     ['anc-wobbly']),
    ('cena-01-b', f'{WOBBLY} tumbling off the bed and landing flat on the floor, comically, legs in the air.',
     ['anc-wobbly']),
    ('cena-02-a', f'{WOBBLY} running, or rather stumbling, through a bright colorful cartoon city looking for work, '
                  f'determined and clumsy.', ['anc-wobbly']),
    ('cena-02-b', f'{WOBBLY} on a pizza delivery scooter flying comically over a fence, pizza box tumbling in the air.',
     ['anc-wobbly']),
    ('cena-03-a', f'{WOBBLY} proudly handing over a messy squashed pizza to a customer at a door, cheerful, '
                  f'holding coins.', ['anc-wobbly']),
    ('cena-03-b', f'{WOBBLY} driving a small red toy car crashing into a lamppost in the colorful city, comic chaos.',
     ['anc-wobbly']),
    ('cena-04-a', f'{WOBBLY} meeting {BOB} on a city street, both excited, Bob proposing a secret mission.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-04-b', f'{WOBBLY} and {BOB} in a small boat sailing toward a mysterious tropical island, then hitting a rock, '
                  f'water splashing, comic.', ['anc-wobbly', 'anc-bob']),
    ('cena-05-a', f'{WOBBLY} and {BOB} digging and searching on the tropical island, falling and laughing, adventurous.',
     ['anc-wobbly', 'anc-bob']),
    ('cena-05-b', f'{WOBBLY} and {BOB} opening a hidden treasure chest full of gold coins and special clothes, '
                  f'jumping with joy.', ['anc-wobbly', 'anc-bob']),
    ('cena-06-a', f'{WOBBLY} back home at night, tired, dirty and happy, flopping onto his bed with a big smile.',
     ['anc-wobbly']),
    ('cena-06-b', f'{WOBBLY} rolling off the bed onto the floor one more time, legs in the air, laughing, '
                  f'comic happy ending.', ['anc-wobbly']),
]

# 6 cenas (A/B) → 6 blocos de narração, o conto redistribuído por cena:
NARRACAO = {
    1: 'Era um dia ensolarado na cidade de Wobbly, onde tudo era colorido e divertido. Wobbly, um bonequinho '
       'amarelo meio molenga, acordou animado. Hoje vai ser o melhor dia de todos! disse ele, pulando da cama '
       'e caindo no chão logo depois.',
    2: 'Depois de levantar, ele decidiu que queria ficar rico. Então saiu correndo, ou melhor, tropeçando, '
       'pela cidade em busca de trabalho. Primeiro, tentou ser entregador de pizza. Acelerou a moto e acabou '
       'voando por cima de uma cerca!',
    3: 'Mesmo assim, conseguiu entregar a pizza, toda bagunçada, mas entregou! Ufa, ganhei dinheiro! comemorou. '
       'Com o dinheiro, comprou um carrinho vermelho. Mas dirigir não era fácil: bateu num poste, numa árvore, '
       'e depois nele mesmo!',
    4: 'No meio da confusão, encontrou seu amigo Bob. Vamos fazer uma missão secreta? disse Bob. Eles aceitaram '
       'o desafio: encontrar um tesouro escondido na ilha misteriosa. Pegaram um barco e foram navegando, '
       'até baterem numa pedra. Mas não desistiram! Nadaram até a ilha.',
    5: 'Depois de muitas quedas, pulos errados e risadas, eles encontraram um baú escondido! Conseguimos! '
       'gritaram juntos. Dentro havia muito dinheiro e roupas especiais!',
    6: 'No final do dia, Wobbly voltou para casa cansado, sujo e feliz. Hoje foi um dia maluco, mas incrível! '
       'disse ele, caindo na cama e no chão de novo. E assim terminou mais um dia na cidade de Wobbly, '
       'onde tudo pode acontecer!',
}

MOVIMENTO = {
    1: 'Wobbly wakes up happily with arms up, then tumbles off the bed onto the floor, comic',
    2: 'Wobbly stumbles through the colorful city, then flies over a fence on the pizza scooter',
    3: 'Wobbly proudly hands over the squashed pizza with coins, then crashes the little red car into a lamppost',
    4: 'Wobbly meets Bob excitedly, then the two sail off in a boat and hit a rock, water splashing',
    5: 'the two search the island falling and laughing, then open the treasure chest and jump with joy',
    6: 'Wobbly flops onto his bed tired and happy, then rolls off onto the floor again, comic ending',
}
