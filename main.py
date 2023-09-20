import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
    else:
        await ctx.send("Вы забыли загрузить картинку :(")


bot.run('MTA5MTc4MDUzMjE0MjA4MDA0OA.Gy4wsr.D9zV7f5zDipDZlpT0A_1ybEbiXGoV0-MSGb-ng')