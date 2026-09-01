# "Luna e a Sereia" (sem título no original)
# Personagens (design inventado): Luna, menina que acredita em sereias; a sereia.
# Tom contemplativo/mágico, praia. Mensagem: acreditar na magia e cuidar do oceano.

TITULO = 'Luna e a Sereia'
LEGENDA = ('Luna e a Sereia\n'
           '8 cenas · imagens agnes-image-2.1-flash · video keyframes agnes-video-v2.0 · '
           'narracao bella local. Custo US$ 0.')
VOZ = 'bella'

LUNA = ('Luna, a young girl about eight years old with long wavy dark hair, wearing a light flowing '
        'summer dress, curious and gentle')
SEREIA = ('a beautiful mermaid with long flowing turquoise hair, a shimmering blue-green fish tail, '
          'kind eyes, gentle smile')
STYLE = ('Pixar-style 3D animated feature film render, soft cinematic lighting, warm golden beach light, '
         'dreamy magical atmosphere, restrained natural saturation')

ANCORAS = [
    ('anc-luna', f'Character reference of {LUNA}, standing on a sunny beach, three-quarter view, full body. '
                 f'Plain soft background.', None),
    ('anc-sereia', f'Character reference of {SEREIA}, in shallow turquoise sea water, three-quarter view. '
                   f'Plain soft ocean background.', None),
]

CENAS = [
    ('cena-01-a', f'{LUNA} standing on the shore watching the sea attentively, hoping to spot something magical '
                  f'among the waves, golden light.', ['anc-luna']),
    ('cena-01-b', f'{LUNA} finding a beautiful spiral seashell in the sand, picking it up with wonder.', ['anc-luna']),
    ('cena-02-a', f'Close-up of {LUNA} holding the seashell to her ear, eyes closing, hearing a soft melody, enchanted.',
     ['anc-luna']),
    ('cena-02-b', f'{LUNA} returning to the beach at dawn, the sea calm and glowing pink and gold, hopeful.', ['anc-luna']),
    ('cena-03-a', f'{SEREIA} appearing among the gentle waves for a few moments, magical shimmer, beautiful.',
     ['anc-sereia']),
    ('cena-03-b', f'{SEREIA} smiling and waving warmly at {LUNA} from the water, a tender magical connection.',
     ['anc-luna', 'anc-sereia']),
    ('cena-04-a', f'{SEREIA} diving gracefully back into the sea, her tail splashing, a trail of sparkles.', ['anc-sereia']),
    ('cena-04-b', f'{LUNA} walking home along the beach at golden hour, very happy, glancing back at the sea, '
                  f'still believing in magic.', ['anc-luna']),
]

NARRACAO = {
    1: 'Era uma vez uma menina chamada Luna, que acreditava em sereias. Sempre que ia à praia, ela observava '
       'o mar com atenção, esperando ver um brilho diferente entre as ondas. Um dia, enquanto caminhava pela '
       'areia, Luna encontrou uma concha muito bonita.',
    2: 'Quando a colocou perto do ouvido, ouviu uma melodia suave que parecia vir do fundo do mar. Curiosa, '
       'ela voltou à praia ao amanhecer.',
    3: 'De repente, viu uma linda sereia aparecer por alguns instantes. A sereia sorriu, acenou para Luna e disse: '
       'Nunca deixe de acreditar na magia e de cuidar do oceano.',
    4: 'Antes que Luna pudesse responder, a sereia mergulhou de volta ao mar. Luna voltou para casa muito feliz. '
       'Ninguém sabia se aquilo tinha sido um sonho ou um encontro de verdade, mas ela nunca deixou de acreditar '
       'que o mundo pode guardar mistérios e maravilhas para quem observa a natureza com carinho.',
}

MOVIMENTO = {
    1: 'Luna watches the waves, then finds the seashell in the sand and lifts it with wonder',
    2: 'Luna holds the shell to her ear hearing the melody, then returns to the glowing dawn beach',
    3: 'the mermaid appears among the waves, then smiles and waves warmly at Luna',
    4: 'the mermaid dives back into the sea with a trail of sparkles, then Luna walks home happy at golden hour',
}
