import colors

default = {
            'back': "'",
            'body': '-',
            'end': '.',
            'indent': False,
            'colored': False}
blocks = {
            'back': "█",
            'body': '█',
            'end': '█',
            'indent': True,
            'colored': False}

blocks_with_colors = {
            'back': "█",
            'body': '█',
            'end': '█',
            'indent': True,
            'colored': True,
            'colors': [ colors.green.text, 
                        colors.green.text,
                        colors.green.text, 
                        colors.green.text, 
                        colors.green.text, 
                        colors.blue.text,
                        colors.white.text,
                        colors.white.text,
                        colors.white.text,
                        colors.white.text,
                        colors.white.text,
                        colors.blue.text,
                        ]
                    }

skins = {
    'default': default,
    'blocks': blocks,
    'colors': blocks_with_colors
}