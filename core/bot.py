from __future__ import annotations
from discord.ext import commands
from datetime import datetime, timedelta
from discord import Interaction
from typing import Optional
from logging import getLogger; log = getLogger("Bot")
from .embed import Embed
from tortoise import Tortoise
from config import *

import discord
import os
import sys

__all__ = (
    "Bot",
)

client = discord.client

def restart_me():
    os.execv(sys.executable, ['pythob'] + sys.argv)

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix= '^',
            intents= discord.Intents.all(),
            chunk_guild_at_startup= False
        )
        
    async def setup_hook(self) -> None:
        for file in os.listdir('cogs'):
            if not file.startswith("_"):
                await self.load_extension(f"cogs.{file}.plugin")
        
    async def on_ready(self) -> None:
        members = 0
        for guild in self.guilds:
             members += guild.member_count - 1

        await self.change_presence(activity=discord.Game(name=f"On {len(self.guilds)} Servers | {VERSION} | /help"))
        log.info(f"Logged in as {self.user} (ID: {self.user.id})")
        self.tree.sync
        
    async def on_connect(self) -> None:
        if '-sync' in sys.argv:
            synced_commands = await self.tree.sync()
            log.info(f"Successfully synced {len(synced_commands)} commands! 🙃")
            
        if datetime.now().hour == 23 and datetime.now().minute == 59:
            restart_me()
    
async def success(
            self,
            message: str,
            interaction: discord.Interaction,
            *,
            ephemeral: Optional[bool] = True,
            embed: Optional[bool] = True
    ) ->Optional[discord.WebhookMessage]:
            if embed:
                if interaction.response.is_done():
                    return await interaction.followup.send(
                        embed=Embed(description=message, color=discord.Colour.from_rgb(
                         r= 8,
                         g= 255,
                         b= 8
                        )),
                        ephemeral=ephemeral
                    )
                return await interaction.response.send_message(
                    embed=Embed(description=message, color=discord.Colour.from_rgb(
                     r= 8,
                     g= 255,
                     b= 8
                    )),
                    ephemeral=ephemeral
                )
            else:
                if interaction.response.is_done():
                    return await interaction.followup.send(content=f"✔️ | {message}", ephemeral=ephemeral)
                return await interaction.response.send_message(content=f"✔️ | {message}", ephemeral=ephemeral)


async def error(
            self,
            message: str,
            interaction: discord.Interaction,
            *,
            ephemeral: Optional[bool] = True,
            embed: Optional[bool] = True
    ) ->Optional[discord.WebhookMessage]:
            if embed:
                if interaction.response.is_done():
                    return await interaction.followup.send(
                        embed=Embed(description=message, color=discord.Colour.from_rgb(
                         r=255, 
                         g= 49, 
                         b= 49
                        )),
                        ephemeral=ephemeral
                    )
                return await interaction.response.send_message(
                    embed=Embed(description=message, color=discord.Colour.from_rgb(
                     r= 255,
                     g= 49,
                     b= 49
                    )),
                    ephemeral=ephemeral
                )
            else:
                if interaction.response.is_done():
                    return await interaction.followup.send(content=f"✖️ | {message}", ephemeral=ephemeral)
                return await interaction.response.send_message(content=f"✖️ | {message}", ephemeral=ephemeral)