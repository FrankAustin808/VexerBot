from __future__ import annotations
import asyncio
import discord
import logging
from core import Bot
from config import *
from discord.ext import commands

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

client = commands.Bot(
    command_prefix='^',description=description, intents=intents)

async def main():
    discord.utils.setup_logging()
    async with Bot() as bot:
        await bot.start(TOKEN, reconnect=True)
        
if __name__ == '__main__':
    asyncio.run(main())