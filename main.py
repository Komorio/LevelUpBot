import discord
import os
import asyncio
import model

from discord.ext import commands
from discord.ext.commands import bot

description = "Level Up Bot"
bot = commands.Bot(command_prefix=":", description=description)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb)

@bot.command()
async def 일정보기(ctx):
    pass

@bot.command()
async def 설명(ctx):
    pass

@bot.command()
async def 명령어(ctx):
    description = ""
    
    for command in model.commands:
        description += command

    embed=discord.Embed(title="🛠 명령어 목록", description=description, color=discord.Color.blue())
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)