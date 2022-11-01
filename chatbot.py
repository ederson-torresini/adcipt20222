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
prefix = '-'
bot = commands.Bot(intents=intents, command_prefix=prefix)


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    #
    # Testar se o autor é um bot (msg.author.bot é verdadeiro)
    # e, se for, simplesmente ignorar a mensagem
    if msg.author.bot:
        return
    autor = msg.author.id
    #
    # Filtrar comando por prefixo
    if msg.content.strip()[0] == prefix:
        mensagem = msg.content.strip()[1:]
    else:
        return
    #
    # Testar se o canal é pvt (msg.channel.type.name == 'private')
    # e, se for, avisar o jogador
    if msg.channel.type.name == 'private':
        await msg.channel.send(frases['canal_privado'])
        return
    #
    # Testar se o jogador está em canal de voz,
    # caso contrário convidá-lo a entrar em um
    if not msg.author.voice:
        await msg.channel.send(frases['sem_canal_de_voz'])
        return
    #
    # Testar se o bot (msg.guild.me)
    # já está conectado no canal de voz do jogador (in msg.author.voice.channel.members),
    # caso contrário conectá-lo
    if msg.guild.me in msg.author.voice.channel.members:
        canal_de_voz = msg._state.voice_clients[0]
    else:
        canal_de_voz = await msg.author.voice.channel.connect()
    #
    # Garantir que o autor tem dados de partida
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
        if fullmatch(key, mensagem):
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
                # Se houver um som referente ao estado,
                # toca no canal de voz do jogador
                som = str(value) + '.opus'
                if exists(som):
                    # canal_de_voz.play(AudioSource)
                    canal_de_voz.play(discord.FFmpegPCMAudio('1.mp3'), after=lambda e: print('done', e))
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
