import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.ext.commands import Bot
from discord.utils import get
from discord import gateway
from random import choice, randint
from discord import Spotify
from imagelink import nekoimage, animehug, animebite, animepat, animelick, animeboop, animecry, kissanime, teaanime
from pymongo import MongoClient
from colorama import Fore      
import json
import requests
import asyncio
import os
import time
import keep_alive
import aiohttp
from discord import FFmpegPCMAudio
import typing
from dotenv import load_dotenv
from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
from Cybernator import Paginator
import io
from googletrans import Translator
from pytube import YouTube 
from discord_together import DiscordTogether
from pypresence import Presence

cluster = MongoClient(os.environ.get('MONGO'))
collection = cluster.ecodb.colldb

def get_prefix(client, message):
    if message.channel != message.author.dm_channel:
        prefix = collection.find_one({"_id": message.guild.id})["prefix"]
        return prefix
    if message.channel == message.author.dm_channel:
        prefix = ">"
        return prefix

#ПРЕФИКС
client = commands.AutoShardedBot(shard_count=6, command_prefix=">", intents=discord.Intents().all())

client.remove_command("help")



@client.command()
async def load(ctx, extension):
  if ctx.author.id == int(os.environ.get('DEVELOPER_ID')):
        client.load_extension(f'cogs.{extension}')
        await ctx.send("Спец. категория была загружена, проблем не зафиксировано!")
  else:
      await ctx.send("Вы не создатель бота!")

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == int(os.environ.get('DEVELOPER_ID')):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send("Спец. категория была перезагружена, проблем не зафиксировано!")
    else:
        await ctx.send("Вы не создатель бота!")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == int(os.environ.get('DEVELOPER_ID')):
        client.unload_extension(f'cogs.{extension}')
        await ctx.send("Спец. категория была выгружена, проблем не зафиксировано!")
    else:
        await ctx.send("Вы не создатель бота!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    DiscordComponents(client)
    bot2 = client.get_user(919865860116590613)
    print(f'🤍Бот: {bot2} запустился!🖤')
    while True:
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"{len(client.guilds)} серверов! | >help"))
        await asyncio.sleep(12)
        await client.change_presence(status=discord.Status.idle,activity=discord.Game(f"{len(set(client.get_all_members()))} участников | >help"))
        await asyncio.sleep(12)

    for guild in client.guilds:
      for member in guild.members:
        post = {
        '_id': member.id,
        'block': 300,
        'xp': 0,
        'lvl': 1
        }

        if collection.count_documents({'_id': member.id}) == 0:
          collection.insert_one(post)

@client.event
async def on_member_join(member):
    post = {
      '_id': member.id,
      'balance': 300,
      'xp': 0,
      'lvl': 1
  }

    if collection.count_documents({'_id': member.id}) == 0:
      collection.insert_one(post)

@client.command()
async def test(ctx):
  await ctx.send(
    embed= discord.Embed(title="Invite to party"),
    components=[
        Button(style=ButtonStyle.green, label="Acept", emoji="🥑"),
        Button(style=ButtonStyle.red, label="Decline", emoji="🌹"),
        Button(style=ButtonStyle.URL,  label="Server", url="https://discord.gg/TSXKNaHS")
    ]
  )
  
  responce = await client.wait_for("button_click")

  if responce.channel == ctx.channel:
    if responce.component.label == "Acept":
      await responce.respond(content="Great! 🥰")

    else:
      await responce.respond(
        embed= discord.Embed(title="Are you sure?"),
       components=[
          Button(style=ButtonStyle.green, label="Yes"),
          Button(style=ButtonStyle.red, label="No"),         
          Button(style=ButtonStyle.blue, label="I`ll think...", emoji="🤔")
       ]
      )


"""RPC = Presence(os.environ['ID'])

btns = [
  {
    "label": "Server",
    "url": "https://discord.gg/CNaVPAuB5S"
  },
  {
    "label": "Server",
    "url": "https://discord.gg/3rJkq7bBZT"
  }
]

RPC.content()
RPC.update(
  state="Фурри *uwu*",
  details="Это пушистый лис",
  start=time(),
  buttons=btns,
  large_image="png-transparent-furry-fandom-art-fansite-fan-mammal-carnivoran-furry-fandom",
  small_image="d6sbo18-47e8314b-4d34-48c8-a2bd-ddbf61d6b8e8e97xiltx",
  large_text="Ты мой фурри *owo*",
  small_text="Ты мой милашка!"
)"""
  
@client.event
async def on_command_error(ctx, error):
    print(f'{Fore.RED}[=====================Ошибка!=====================]{Fore.RESET}\nАвтор получивший ошибку: {Fore.YELLOW}{ctx.author}{Fore.RESET}\nСодержание сообщения: {Fore.YELLOW}{ctx.message.content}{Fore.RESET}\nДата происшествия: {Fore.YELLOW}{ctx.message.created_at.day}.{ctx.message.created_at.month}.{ctx.message.created_at.year}{Fore.RESET}\nОшибка: {Fore.YELLOW}{str(error).replace("Command raised an exception:", "", 1)}{Fore.RESET}')

# Запуск севера
keep_alive.keep_alive()

# Логин бота
client.run(os.environ.get('Token'))