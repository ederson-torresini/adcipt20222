from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from random import choice
from re import search
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')

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


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    #
    # Armazenar o autor da mensagem.
    autor = msg.author.id

    # Verificar se a mensagem não tem o próprio bot como autor.
    if autor == bot.application_id:
        return
    #
    # Verificar se o jogador ainda não começou a partida,
    # o que significa que precisa colocá-lo no estado zero (0).
    if autor not in partidas:
        partidas[autor] = 0
    #
    # Em ordem de operação:
    # 0) Obter o estado atual do jogador:
    #    partidas[autor]
    # 1) Obter a definição completa desse estado:
    #    estados[partidas[autor]]
    estado_do_jogador = estados[partidas[autor]]
    #
    # 3) Filtrar desse estado apenas a lista de próximos estados:
    #    estados_do_jogador['proximos_estados']
    # 4) Obter a lista completa dos próximos estados:
    #    estado_de_jogador['proximos_estados'].items()
    # 5) Separar chave e valor da lista completa:
    for key, value in estado_do_jogador['proximos_estados'].items():
        #
        # Comparar a frase do jogador com a chave usando expressões regulares:
        if search(key, msg.content):
            #
            # Atualizar o estado do jogador,
            # e para isso é usado o conteúdo da mensagem como valor do dicionário:
            partidas[autor] = value
            #
            # A definição completa do estado do jogador,
            # por consequência, também é atualizada
            estado_do_jogador = estados[partidas[autor]]
            #
            # Enviar para o jogador a mensagem do estado (já atualizado)
            #
            # Em ordem de operação:
            # 0) Filtrar do estado do jogador apenas a lista de frases:
            #    estado_do_jogador['frases']
            # 1) Sortear uma frase dessa lista:
            #   choice(estado_do_jogador['frases'])
            await msg.channel.send(choice(estado_do_jogador['frases']))
            #
            # Retonar a função, já que a resposta ao jogador já foi dada.
            return
    #
    # Caso contrário, avisar que a mensagem não avança no jogo.
    # Se o jogador ainda estiver no estado, ajudar com uma dica:
    if partidas[autor] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        #
        #  Nos estados seguintes, a resposta padrão de HAL:
        await msg.channel.send('I\'m sorry Dave, I\'m afraid I can\'t do that.')


bot.run(getenv('DISCORD_TOKEN'))
