import discord
from discord.ext import commands
import random
import logging
import logging.handlers



description = '''Vexer is a bot that updates all users on Tool updates from Treaus Tools!'''

intents  = discord.Intents.all()
intents.members = True
intents.message_content = True

handler = logging.FileHandler(
    filename='discord.log', 
    encoding='utf-8', 
    mode='w',
    maxBytes=32 * 1024 * 1024,
    backupCount= 5
    )

bot = commands.Bot(command_prefix='^',description=description, intents=intents )

TOKEN = ''

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event 
async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.context.startswith('^hello'):
            await message.reply('Hello', mention_author=True)

bot.run(TOKEN, log_handler=handler)