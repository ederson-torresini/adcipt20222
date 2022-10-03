# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
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
        }
    },
    2: {
        'frases': ['Era uma vez...', 'E lá de volta outra vez...'],
        'proximos_estados': {
            '[nN][aã]+o': 3
        }
    },
    3: {
        'frases': ['Fim do jogo!', 'Parabéns!'],
        'proximos_estados': {
            '[rR]einicia(r)*': 1
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}
