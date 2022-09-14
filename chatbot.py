from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="")


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Verificar se a mensagem não tem o próprio bot como autor
    if msg.author.id != msg.channel.me.id:
        await msg.channel.send("oi")

bot.run(getenv("DISCORD_TOKEN"))
