from definições import estados, partidas
import discord
from discord.ext import commands
from random import choice
from re import fullmatch
from datetime import datetime, timedelta
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
    autor = msg.author.id
    if autor == bot.application_id:
        return

    if autor not in partidas:
        partidas[autor] = {'estado': 0, 'ultima_mensagem': msg.created_at}

    estado_do_jogador = estados[partidas[autor]['estado']]
    ultima_mensagem = partidas[autor]['ultima_mensagem']

    for key, value in estado_do_jogador['proximos_estados'].items():
        if fullmatch(key, msg.content):

            delta = msg.created_at - ultima_mensagem
            if delta.seconds > estado_do_jogador['tempo_limite']:
                await msg.channel.send('Tempo limite estourado. Reiniciando o jogo...')
                partidas[autor] = {'estado': 1, 'ultima_mensagem': msg.created_at}
            else:
                partidas[autor]['estado'] = value
                partidas[autor]['ultima_mensagem'] = msg.created_at

            estado_do_jogador = estados[partidas[autor]['estado']]                #

            await msg.channel.send(choice(estado_do_jogador['frases']))
            return

    if partidas[autor]['estado'] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send('I\'m sorry Dave, I\'m afraid I can\'t do that.')


bot.run(getenv('DISCORD_TOKEN'))
