import discord
from discord.ext import commands
import random



description = '''Vexer is a bot that updates all users on Tool updates from Frank!'''

intents  = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='^',description=description, intents=intents )

TOKEN = ''

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(TOKEN)