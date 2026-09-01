# "Luna e o Segredo do Oceano" — CONTINUAÇÃO de luna.py
# Reusa Luna e a sereia (âncoras semeadas de output/luna). Tema: cuidar do oceano.

TITULO = 'Luna e o Segredo do Oceano'
LEGENDA = ('Luna e o Segredo do Oceano (continuacao)\n'
           'imagens agnes-image-2.1-flash · video keyframes · narracao bella local. Custo US$ 0.')
VOZ = 'bella'

LUNA = ('Luna, a young girl about eight years old with long wavy dark hair, wearing a light flowing '
        'summer dress, curious and gentle')
SEREIA = ('a beautiful mermaid with long flowing turquoise hair, a shimmering blue-green fish tail, '
          'kind eyes, gentle smile')
STYLE = ('Pixar-style 3D animated feature film render, soft cinematic lighting, warm golden beach light, '
         'dreamy magical atmosphere, restrained natural saturation')

ANCORAS = []   # reusadas do filme 1 (anc-luna, anc-sereia)

CENAS = [
    ('cena-01-a', f'{LUNA} walking on the beach at dawn again, hoping to see the mermaid, holding her seashell.',
     ['anc-luna']),
    ('cena-01-b', f'{LUNA} finding the beach covered in washed-up plastic and trash, sad and worried.', ['anc-luna']),
    ('cena-02-a', f'{SEREIA} appearing among the waves looking tired and sad, the polluted water around her.',
     ['anc-sereia']),
    ('cena-02-b', f'{LUNA} starting to pick up the trash from the sand, determined to help, the mermaid watching gratefully.',
     ['anc-luna', 'anc-sereia']),
    ('cena-03-a', f'{LUNA} with other children joining to clean the whole beach together, teamwork, hopeful.',
     ['anc-luna']),
    ('cena-03-b', f'The sea turning clear and bright blue again, fish and dolphins returning, {SEREIA} happy and glowing.',
     ['anc-sereia']),
    ('cena-04-a', f'{SEREIA} giving {LUNA} a glowing pearl as a thank-you gift, a tender magical moment.',
     ['anc-luna', 'anc-sereia']),
    ('cena-04-b', f'{LUNA} watching the healthy shining sea at golden hour, holding the pearl, proud and happy, ending.',
     ['anc-luna']),
]

NARRACAO = {
    1: 'Luna voltou à praia ao amanhecer, esperando rever sua amiga sereia. Mas, ao chegar, encontrou a areia '
       'coberta de lixo e plástico trazidos pelo mar. Que tristeza, pensou ela.',
    2: 'A sereia apareceu entre as ondas, cansada e triste, pois o oceano estava sujo. Sem dizer nada, Luna '
       'começou a recolher o lixo da areia, decidida a ajudar.',
    3: 'Logo, outras crianças vieram ajudar, e juntas limparam a praia inteira. Aos poucos, o mar voltou a ficar '
       'claro e azul, e os peixes e golfinhos retornaram.',
    4: 'Feliz, a sereia deu a Luna uma pérola brilhante como agradecimento. Luna aprendeu que cuidar da natureza '
       'é o maior mágica de todas, e nunca mais deixou de proteger o oceano.',
}

MOVIMENTO = {
    1: 'Luna walks the dawn beach hopeful, then finds it covered in washed-up trash, saddened',
    2: 'the tired mermaid appears in the waves, then Luna begins picking up the trash, determined',
    3: 'other children join to clean the beach, then the sea turns clear blue and the fish return',
    4: 'the mermaid gives Luna a glowing pearl, then Luna watches the healthy sea at golden hour, proud',
}
