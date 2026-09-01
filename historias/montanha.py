# "O Menino Perdido na Montanha"
# Elenco: Lucas (11), Atlas (são-bernardo de resgate), pais, equipe de resgate.
# Clima Pixar, drama de sobrevivência infantil — sem violência gráfica.

TITULO = 'O Menino Perdido na Montanha'
LEGENDA = ('O Menino Perdido na Montanha\n'
           '14 cenas · imagens agnes-image-2.1-flash · video keyframes agnes-video-v2.0 · '
           'narracao bella local. Custo US$ 0.')
VOZ = 'bella'

LUCAS = ('Lucas, an eleven-year-old boy with short brown hair, wearing a red winter coat, '
         'blue snow pants, a wool hat and gloves')
ATLAS = ('Atlas, a large Saint Bernard rescue dog with white and brown fur, gentle dark eyes, '
         'wearing a rescue vest with small pouches')
PAIS = ("Lucas's parents, an adult man and an adult woman in warm winter jackets, worried and loving")
RESGATE = ('three mountain rescuers in red jackets with backpacks and trekking poles, professional')

# Model sheet: mãe em text2img; demais vistas derivadas (mesmo indivíduo).
ANCORAS = [
    ('anc-lucas', f'Character reference of {LUCAS}, standing in a snowy pine forest, three-quarter view, '
                  f'full body. Plain soft background.', None),
    ('anc-atlas', f'Character reference of {ATLAS}, standing in deep snow, three-quarter view, full body, '
                  f'the flat rescue vest clearly visible. Plain soft snowy background.', None),
    ('anc-pais', f'Character reference of {PAIS}, standing together at a campsite, three-quarter view, full body.',
     'anc-lucas'),
]

CENAS = [
    # abertura — a montanha bonita
    ('cena-01-a', 'Wide establishing shot of a beautiful winter mountain covered in tall pine trees, '
                  'small streams between rocks, first snow on the path, morning light, majestic.', []),
    ('cena-01-b', f'{LUCAS} arriving with his parents at the foot of the mountain, looking up in wonder, '
                  f'campsite gear around them.', ['anc-lucas', 'anc-pais']),
    # o pássaro azul
    ('cena-02-a', f'{LUCAS} noticing a bright blue bird flying between the pine trees, enchanted, raising a camera.',
     ['anc-lucas']),
    ('cena-02-b', f'{LUCAS} following the blue bird deeper among the trees, the campsite shrinking far behind him.',
     ['anc-lucas']),
    # perdido
    ('cena-03-a', f'{LUCAS} realizing he is lost, turning around, no campsite in sight, calling out, worried.',
     ['anc-lucas']),
    ('cena-03-b', 'Wide shot of the mountain as heavy snow starts falling and thick fog rolls in, '
                  'the boy tiny and alone among identical snowy paths, his bootprints vanishing.', ['anc-lucas']),
    # a noite gelada
    ('cena-04-a', f'{LUCAS} sheltering in a gap between two big rocks and pines at dusk, '
                  f'gathering dry leaves and branches, shivering.', ['anc-lucas']),
    ('cena-04-b', f'Close-up of {LUCAS} at night hugging his knees, teeth chattering, fingers numb, '
                  f'snow falling heavily around him, cold blue moonlight.', ['anc-lucas']),
    # o amanhecer, fraco
    ('cena-05-a', f'Dawn breaking over the snowy forest, {LUCAS} weak and half-buried in snow up to his knees, '
                  f'barely able to stand, pale morning light.', ['anc-lucas']),
    ('cena-05-b', 'A huge shadow appearing in the mist between the snowy trees, mysterious, hopeful.', []),
    # Atlas chega
    ('cena-06-a', f'{ATLAS} emerging from the fog, walking with effort through the deep snow toward the boy.',
     ['anc-atlas']),
    ('cena-06-b', f'{ATLAS} gently pressing his nose against the face of {LUCAS}, tender moment of rescue.',
     ['anc-lucas', 'anc-atlas']),
    # o colete salva
    ('cena-07-a', f'{LUCAS} wrapped in a shiny thermal blanket, drinking from a bottle, {ATLAS} beside him, '
                  f'a little strength returning, warm relief.', ['anc-lucas', 'anc-atlas']),
    ('cena-07-b', f'{LUCAS} hugging {ATLAS}, sharing the dog warmth in the snow, grateful, close.',
     ['anc-lucas', 'anc-atlas']),
    # o apito
    ('cena-08-a', f'{LUCAS} blowing a rescue whistle hard, cheeks puffed, {ATLAS} barking beside him, '
                  f'sound cutting through the snowy forest.', ['anc-lucas', 'anc-atlas']),
    ('cena-08-b', f'{RESGATE} appearing between the snowy trees, waving, having heard the whistle, hopeful.',
     ['anc-atlas']),
    # o resgate
    ('cena-09-a', f'The rescuers wrapping {LUCAS} in more blankets and gently placing him on a snow rescue sled, '
                  f'{ATLAS} watching over him.', ['anc-lucas', 'anc-atlas']),
    ('cena-09-b', f'The rescue team pulling the sled with {LUCAS} through the snow toward safety, {ATLAS} leading.',
     ['anc-lucas', 'anc-atlas']),
    # o reencontro
    ('cena-10-a', f'{LUCAS} arriving at a warm rescue shelter, his parents running toward him with open arms.',
     ['anc-lucas', 'anc-pais']),
    ('cena-10-b', f"{LUCAS} tightly hugged by his parents, the father crying, warm reunion inside the shelter.",
     ['anc-lucas', 'anc-pais']),
    # descanso
    ('cena-11-a', f'{LUCAS} resting by a fireplace under a blanket with a bowl of hot soup, cozy shelter, '
                  f'{ATLAS} lying calmly by the door.', ['anc-lucas', 'anc-atlas']),
    ('cena-11-b', f'{LUCAS} kneeling in front of {ATLAS}, stroking his head, thanking him, emotional, '
                  f'the dog licking his face.', ['anc-lucas', 'anc-atlas']),
    # aprendizado
    ('cena-12-a', f'{LUCAS} back home safe, looking at mountain safety gear, a whistle and a map, thoughtful, '
                  f'having learned his lesson.', ['anc-lucas']),
    ('cena-12-b', f'Years later, {LUCAS} returning to the snowy mountain to visit {ATLAS}, the two reunited '
                  f'and happy in the snow, golden light, ending.', ['anc-lucas', 'anc-atlas']),
]

NARRACAO = {
    1: 'Lucas tinha onze anos e adorava aventuras. Em uma manhã de inverno, ele foi com seus pais conhecer '
       'uma montanha coberta de pinheiros. A paisagem era linda: as árvores pareciam tocar o céu, e a neve '
       'começava a cobrir o caminho.',
    2: 'Enquanto seus pais organizavam o acampamento, Lucas viu um pássaro azul voando entre as árvores. '
       'Encantado, resolveu segui-lo para tirar uma fotografia. Vou só até ali, pensou.',
    3: 'Mas o pássaro voou para outra árvore, e outra, levando Lucas cada vez mais longe. Quando percebeu, '
       'já não conseguia enxergar o acampamento. Pai! Mãe! Apenas o eco respondeu. A neve começou a cair com '
       'mais força, e uma névoa espessa tomou conta da montanha.',
    4: 'Lucas caminhou durante horas, chamando pelos pais. Encontrou um espaço entre duas grandes pedras e se '
       'protegeu do vento, mas não conseguiu acender uma fogueira. A temperatura continuava caindo.',
    5: 'Quando o dia começou a clarear, Lucas estava fraco e quase não conseguia se levantar. A neve chegava '
       'perto dos seus joelhos. Socorro, ele tentou gritar, mas sua voz saiu baixa e rouca.',
    6: 'De repente, ouviu um som distante. No meio da neblina surgiu uma enorme sombra: era um cão grande, '
       'de pelo branco e marrom. Um são-bernardo. Seu nome era Atlas, e ele fazia parte de uma equipe de resgate.',
    7: 'Preso ao corpo do cachorro havia um colete com pequenas bolsas. Lucas encontrou um cobertor térmico e '
       'uma garrafa com uma bebida morna. Ele se enrolou no cobertor e bebeu devagar. O líquido morno aqueceu '
       'seu corpo. Obrigado, Atlas, sussurrou.',
    8: 'No colete também havia um apito. Lucas soprou três vezes, o sinal internacional de pedido de socorro. '
       'O som agudo atravessou a floresta. Pouco depois, uma resposta surgiu ao longe. Os socorristas tinham escutado.',
    9: 'Minutos depois, três pessoas apareceram entre as árvores, com roupas vermelhas. Encontramos o menino! '
       'Eles envolveram Lucas em cobertores e o colocaram com cuidado em uma maca própria para a neve.',
    10: 'Quando chegou ao abrigo, Lucas viu seus pais correndo em sua direção. Sua mãe o abraçou com força, e '
        'seu pai não conseguiu segurar as lágrimas. Eles nunca desistiram de procurá-lo.',
    11: 'Lucas tomou uma sopa quente e descansou perto de uma lareira. Antes de ir embora, ajoelhou-se diante '
        'do cachorro e disse: Você salvou minha vida. Nunca vou me esquecer de você.',
    12: 'Depois daquela aventura, Lucas aprendeu que a montanha podia ser bonita, mas também perigosa. E todos '
        'os anos ele voltava à montanha para visitar o seu grande amigo Atlas, o corajoso são-bernardo que '
        'apareceu no meio da neve quando ele mais precisava.',
}

MOVIMENTO = {
    1: 'the camera sweeps across the majestic snowy mountain, then finds the boy and his parents arriving in wonder',
    2: 'the boy spots the blue bird and follows it among the trees, the campsite shrinking behind him',
    3: 'the boy turns around lost and calls out, then heavy snow and fog swallow the mountain around him',
    4: 'the boy shelters between the rocks gathering branches, then hugs his knees shivering in the night snow',
    5: 'dawn light grows over the weak boy in deep snow, then a huge shadow appears in the mist',
    6: 'the Saint Bernard emerges from the fog and walks to the boy, gently pressing his nose to his face',
    7: 'the boy wraps in the thermal blanket and drinks, strength returning, then hugs the dog for warmth',
    8: 'the boy blows the whistle hard while the dog barks, then the rescuers appear waving between the trees',
    9: 'the rescuers wrap the boy and place him on the sled, then pull him through the snow to safety',
    10: 'the boy arrives at the shelter and his parents run to him, embracing tightly, the father crying',
    11: 'the boy rests by the fire with soup, then kneels to thank the dog who licks his face',
    12: 'the boy looks at safety gear thoughtfully, then years later reunites happily with Atlas in the snow',
}
