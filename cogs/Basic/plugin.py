import discord
import datetime
import discord
from .. import Plugin
from typing import Optional
from discord import Member, User, Message
from discord.ext import commands
from core import *
from discord import Interaction, app_commands, Permissions
from discord.ui import View, Select
from config import VERSION
from typing import Optional
from discord.ext import commands, tasks
from logging import getLogger
from tortoise import Tortoise
from cogs import *

class Basic(Plugin):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        
    @app_commands.command(
        name='msg-formatting',
        description= "Shows Discord's message formatting!"
    )
    async def message_formatting(self, interaction: Interaction):
        await interaction.response.send_message('''
# ***Discord Message Formatting***

## **Headers**

> Add # Before Text For Large Header.

> Add ## Before Text For Medium Header.

> Add ### Before Text For Small Header.

### **Examples**

> # Large Header.
> ## Medium Header.
> ### Small Header.

## Text Formatting

### *Remember Close The Asterisks*

### These Can Be Combined!

### *Italics*
> Italics: - One Asterisk [ * ] Before / After Text.

### **Bold**
> Bold: - Two Asterisks [ * ] Before / After Text.

### ***Bold italics***
> Bold Italics: - Three Asterisks [ * ] Before / After Text.

### __Underline__
> Underline: - Two Underscore Symbols [ _ ] Before / After Text.

### ~~Strikethrough~~
> Strikethrough: - Two Tilde Symbols [ ~ ] Before / After Text.

### ||BOO! Spoiler Message 👻||
> Spoiler: - Two Verticle Bars [ | ] Before / After Text.

## **Lists**

**List Option One: * **

**List Option Two: -**

### **Examples**

> Option One:
> * List Item One
> 
> Option Two:
> - List Item Two

## **Code Blocks**

> Single Line Code Block: Start And End Your Message With A Backtick Symbol [ ` ]
> 
> Multi-Line Code Block: Start And End Your Message With Three Backtick Symbols [ ` ]
> 
> Multi-Line Code Block With Language: Start Your Message With Three Backtick Symbols Then Type The Language Name Then End Your Message With Three Backtick Symbols [ ` ] ( Example: Python = Python or py )

### **Examples**

` Test Single Line Code Block `

```
Test Multi-Line Code Block

```
```python
    async def on_ready(self) -> None:
        log.info("Test Multi-Line Code Block With Language")
        self.tree.sync
```

## **Block Quotes**

**If You Want To Add A Single Block Quote, Just Add (>) Before The First Line. **
***For Example:***

> Test

**If You Want To Add Multiple Lines To A Single Block Quote, Just Add (>>>) Before The First Line. **
***For Example:***

>>> Test
Hello 
How Are Ya?
''', ephemeral=True)
    
    @app_commands.command(
        name='bug',
        description="Report a bug you have found!"
    )
    async def bug_command(self, interaction: Interaction):
        embed = Embed(
            description=f"Found a bug? Awesome, please report [here](https://github.com/FrankAustin808/ConsoleBot/issues)! :smiley:"
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(
        name='embed',
        description="Create a custom embed message"
    )
    @app_commands.describe(
        message="Write Your Message"
    )
    async def embed_command(self, interaction: Interaction, message: str = None):
        embed = Embed(color=discord.Colour.random())
        embed.set_author(name=interaction.user, url=interaction.user.avatar)
        embed.add_field(name="", value=message)
        embed.set_footer(text=interaction.guild,
                         icon_url=interaction.guild.icon)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(
        name='membercount',
        description="Shows the amount of members in the guild"
    )
    async def membercount_command(self, interaction: Interaction):
        embed = Embed(color=discord.Colour.random())
        embed.set_author(name=f"Caine",
                         icon_url=self.bot.user.avatar)
        embed.add_field(name="Current Member Count: ",
                        value=interaction.guild.member_count)
        embed.set_footer(text=interaction.guild,
                         icon_url=interaction.guild.icon)
        embed.timestamp = datetime.datetime.now()

        await interaction.response.send_message(embed=embed, ephemeral=True)
    
async def setup(bot: Bot):
    await bot.add_cog(Basic(bot))