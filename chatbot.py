from definições import frases, estados, partidas
import discord
from discord.ext import commands
from random import choice
from re import fullmatch
from os import getenv
from os.path import exists
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    #
    # Testar se o autor é um bot (incluindo o próprio)
    if msg.author.bot:
        return
    #
    # Garantir que o autor tem dados de partida
    autor = msg.author.id
    if autor not in partidas:
        #
        # Jogador começa no estado 0 com duas chaves
        partidas[autor] = {
            'estado': 0,
            'inventario': {
                'chave_prateada',
                'chave_dourada'
            }
        }
    #
    # Criar variáveis locais para melhorar legibilidade do código
    estado_do_jogador = estados[partidas[autor]['estado']]
    inventario_do_jogador = partidas[autor]['inventario']
    #
    # Varrer os possíveis próximos estados para validar com a mensagem do usuário
    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, msg.content):
            #
            # Verificar se o jogador possui inventário mínimo para avançar
            if inventario_do_jogador.issuperset(estados[value]['inventario']):
                #
                # Atualiza o estado do jogador
                partidas[autor]['estado'] = value
                #
                # Remove os itens de inventário requisitados
                partidas[autor]['inventario'] = inventario_do_jogador.difference(
                    estados[value]['inventario'])
                #
                # Se houver uma imagem referente ao estado,
                # envia essa primeiro
                imagem = str(value) + '.png'
                if exists(imagem):
                    await msg.channel.send(file=discord.File(imagem))
                #
                # Cria uma lista de frases usando o delimitador '|' e envia uma a uma
                [await msg.channel.send(i) for i in choice(estados[value]['frases']).split('|')]
            else:
                #
                # Retornar mensagem (e manter jogador no atual estado)
                await msg.channel.send(frases['inventario_insuficiente'])
            return
    #
    # Sempre responder ao usuário (dica ou não)
    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])


bot.run(getenv('DISCORD_TOKEN'))
