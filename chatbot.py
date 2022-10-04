from definições import frases, estados, partidas
import discord
from discord.ext import commands
from random import choice
from re import fullmatch
from os import getenv
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
    # Testar se o autor é um bot (incluindo o próprio)
    if msg.author.bot:
        return

    autor = msg.author.id
    if autor not in partidas:
        # Jogador começa no estado 0 com duas chaves
        partidas[autor] = {
            'estado': 0,
            'inventario': {
                'chave_prateada',
                'chave_dourada'
            }
        }

    estado_do_jogador = estados[partidas[autor]['estado']]
    inventario_do_jogador = partidas[autor]['inventario']

    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, msg.content):
            if inventario_do_jogador.issuperset(estados[value]['inventario']):
                # Atualiza o estado do jogador
                partidas[autor]['estado'] = value
                # Remove os itens de inventário requisitados
                partidas[autor]['inventario'] = inventario_do_jogador.difference(
                    estados[value]['inventario'])
                await msg.channel.send(choice(estados[value]['frases']))
            else:
                await msg.channel.send(frases['inventario_insuficiente'])
            return

    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send(frases['erro'])


bot.run(getenv('DISCORD_TOKEN'))
