import discord
from discord.ext import commands
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
from discord_components import *
from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
from Cybernator import Paginator
import io
from googletrans import Translator
from pytube import YouTube 

cluster = MongoClient(os.environ.get('MONGO'))
collection = cluster.ecodb.colldb

def get_prefix(client, message):
    if message.channel != message.author.dm_channel:
        prefix = collection.find_one({"_id": message.guild.id})["prefix"]
        return prefix
    if message.channel == message.author.dm_channel:
        prefix = ">"
        return prefix

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
      developer = self.client.get_user(888846101531213824)
      embed1 = discord.Embed(description=f'🤍<:1002blurplelike:926901578496102460> • `⠀⠀⠀⠀⠀⠀⠀НАЧАЛО⠀⠀⠀⠀⠀⠀⠀`\n\n Добро пожаловать на главную страницу FurryDragon\n\n<:9390blurpleleave:926823489330118726> <:3199blurplejoin:926823489275584542> Предыдущая страница!\n<:3199blurplejoin:926823489275584542> <:3199blurplejoin:926823489275584542> Следующая страница!\n<:3697crosspink:926830311076159538> <:3199blurplejoin:926823489275584542> Закрыть панель помощи!\n\n Можете писать в лс владельцу бота ({developer.name}#{developer.discriminator}), вопросы задавайте, или спрашивайте и что важное и касается бота, то пишите, если подружиться скажатите ему, он будет рад в знакомстве!\n<:8512blurplelink:926841430792634428>__[ПРИГЛАСИТЬ БОТА](https://discord.com/api/oauth2/authorize?client_id=919865860116590613&permissions=8&scope=bot)<:1113blurpleplus:926837385055051826>', color = discord.Color.from_rgb(255, 215, 0))
      embed2 = discord.Embed(description=f'**ИНФОРМАЦИЯ**\n\n`>help` - команда помощи!\n`>bot` - информация о боте!\n`>profile` - узнаете свой профиль или у другого человека!\n`>avatar` - вы узнаете свою аватарку или у другого человека!\n`>server` - вы узнаете информаацию об сервере!\n`>spotify` - вы узнаете, что вы слушаете в спотифае или у человека!\n`>idea` - вы отправите сообщение об идее!\n`>bug` - вы отправите сообщение об баге!', color = discord.Color.from_rgb(255, 215, 0))
      embed3 = discord.Embed(description=f'**ИНТЕРЕСНОЕ**\n\n`>dog` - рандомные картинки собак\n`>ping` - показывает задержку\n`>cat` - рандомные картинки котов\n`>fox` - рандомные картинки лис\n`>say` - сказать, что-то через ботаn', color = discord.Color.from_rgb(255, 215, 0))
      embed4 = discord.Embed(description=f'**РЕАКЦИЯ**\n\n`>hug` - обнял участника!\n`>boop` - бипнул участника!\n`>kiss` - поцеловал участника!\n`>cry` - плачет от  участника!\n`>tea` - пьёт чай с участником!\n`>lick` - лизнул участника!\n`>bite` - укусила участника!\n`>pat` - погладил участника!', color = discord.Color.from_rgb(255, 215, 0))
      embed5 = discord.Embed(description=f'**МОДЕРАЦИЯ**\n\n`>ban` - банит участника\n`>kick` - выганяет участника', color = discord.Color.from_rgb(255, 215, 0))
      embed7 = discord.Embed(description=f'**КАРТИНКИ/ГИФКИ**\n\n`>neko` - показывает картинки неко!\n`>furry` - рандомные картинки фурри `uwu`!', color = discord.Color.from_rgb(255, 215, 0))
    
      embeds = [embed1, embed2, embed3, embed4, embed5, embed7]
      msg = await ctx.send(embed=embed1)
      reactions = ["<:9390blurpleleave:926823489330118726>","<:3199blurplejoin:926823489275584542>"]
      page = Paginator(self.client, message=msg,only=ctx.author,timeout=90,reactions=reactions,use_exit=True,exit_reaction=["<:3697crosspink:926830311076159538>"],delete_message=True,footer=False, embeds=embeds)
      await page.start() 
      


def setup(client):
    client.add_cog(help(client))
    print(f"{Fore.GREEN}Cog 'help' load!{Fore.RESET}")