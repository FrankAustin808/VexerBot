from __future__ import annotations

import discord
import datetime
import discord
from .. import Plugin
from typing import Optional
from discord import Member, User, Message
from discord.ext import commands
from core import Bot, Embed
from discord import Interaction, app_commands
from discord.ui import View, Select
from config import VERSION
from typing import Optional
from discord.ext import commands, tasks
from logging import getLogger
from tortoise import Tortoise
from cogs import *

class Help(Plugin):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name='help',
        description="Help for ConsoleBot!"
    )
    async def help_command(self, interaction: Interaction):
        embed = Embed(color=discord.Colour.random())

        embed.set_author(name="ConsoleBot's Help Command", url=self.bot.user.avatar)

        embed.set_thumbnail(url=interaction.user.avatar.url)

        embed.add_field(name="Basic", value="/basic")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
async def setup(bot: Bot) -> None:
    await bot.add_cog(Help(bot))