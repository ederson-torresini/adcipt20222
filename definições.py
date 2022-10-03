frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]nicia(r)*': 1
        }
    },
    1: {
        'frases': ['Olá!', 'Tudo bem, como vai?'],
        'proximos_estados': {
            '[sS](i)+m': 2,
            '[nN][aã]+o': 3
        },
        'inventario': {'chave_prateada'}
    },
    2: {
        'frases': ['Era uma vez...', 'E lá de volta outra vez...'],
        'proximos_estados': {
            '[nN][aã]+o': 3
        },
        'inventario': {}
    },
    3: {
        'frases': ['Fim do jogo!', 'Parabéns!'],
        'proximos_estados': {
            '[rR]einicia(r)*': 1
        },
        'inventario': {'chave_dourada'}
    }
}

partidas = {}
