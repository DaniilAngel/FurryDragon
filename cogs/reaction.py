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

class reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fox(self,ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text) 
        embed = discord.Embed(color = 0xff9900, title = 'Лис')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed)
    
    @commands.command()
    async def dog(self,ctx):
        response = requests.get('https://some-random-api.ml/img/dog')
        json_data = json.loads(response.text) 
    
        embed = discord.Embed(color = 0xff9900, title = 'Собака')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed)
    
    
    @commands.command()
    async def cat(self,ctx):
        response = requests.get('https://some-random-api.ml/img/cat')
        json_data = json.loads(response.text) 
    
        embed = discord.Embed(color = 0xff9900, title = 'котов')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed)
    
    
    
    
    @commands.command()
    async def neko(self,ctx):
      ch = choice(nekoimage)
      embed = discord.Embed(title='NEKO | НЕКО', url = ch, color = discord.Color.from_rgb(255, 215, 0))
      embed.set_image(url=f'{ch}')
      await ctx.send(embed=embed)
    
    
    
    
    @commands.command()
    async def furry(self,ctx):
      ch = choice(furry)
      embed = discord.Embed(title='FURRY | ФУРРИ', url = ch, color = discord.Color.from_rgb(255, 215, 0))
      embed.set_image(url=f'{ch}')
      await ctx.send(embed=embed)
    
    
    @commands.command()
    async def hug(self,ctx, member: discord.Member = None, *, reason = None):
      if member != None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} обнял(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animehug)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} обнял(-а) всех!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animehug)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == ctx.author and member != None:
          embed = discord.Embed(description=f'**{ctx.author.mention} обнял(-а) себя... (￢_￢;)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          await ctx.send(embed=embed)
    
    @commands.command()
    async def bite(self,ctx, member: discord.Member = None, *, reason = None):
      if member != None and member != ctx.author:
        embed = discord.Embed(description=f'**{ctx.author.mention} укусил(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
        embed.set_image(url=f'{choice(animebite)}')
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
      if member == None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} укусил(-а) всех!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animebite)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == ctx.author and member != None:
          embed = discord.Embed(description=f'**{ctx.author.mention} укусил(-а) себя... что? (＃￣0￣)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          await ctx.send(embed=embed)
    
    @commands.command()
    async def pat(self,ctx, member: discord.Member = None, *, reason = None):
      if member != None and member != ctx.author:
        embed = discord.Embed(description=f'**{ctx.author.mention} погладил(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
        embed.set_image(url=f'{choice(animepat)}')
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
      if member == None and member != ctx.author:
        embed = discord.Embed(description=f'**{ctx.author.mention} погладил(-а) всех!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
        embed.set_image(url=f'{choice(animepat)}')
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)
      if member == ctx.author and member != None:
        embed = discord.Embed(description=f'**{ctx.author.mention} погладил(-а) себя... (＃￣ω￣)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def lick(self,ctx, member: discord.Member = None, *, reason = None):
      if member != None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} лизнул(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animelick)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} лизнул(-а) всех!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animelick)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == ctx.author and member != None:
          embed = discord.Embed(description=f'**{ctx.author.mention} лизнул(-а) себя... стоп что!? (＞ｍ＜)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          await ctx.send(embed=embed)
    
    @commands.command()
    async def boop(self,ctx, member: discord.Member = None, *, reason = None):
      if member != None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} бупнул(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animeboop)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == None and member != ctx.author:
          embed = discord.Embed(description=f'**{ctx.author.mention} бупнул(-а) всех!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          embed.set_image(url=f'{choice(animeboop)}')
          embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
          await ctx.send(embed=embed)
      if member == ctx.author and member != None:
          embed = discord.Embed(description=f'**{ctx.author.mention} бупнул(-а) себя... всмысле? (￣□￣」)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
          await ctx.send(embed=embed)
    
    @commands.command()
    async def kiss(self,ctx, member: discord.Member = None, *, reason = None):
        if member != None and member != ctx.author:
            embed = discord.Embed(description=f'**{ctx.author.mention} поцеловал(-а) {member.mention}\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
            embed.set_image(url=f'{choice(kissanime)}')
            embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if member == None and member != ctx.author:
            embed = discord.Embed(description=f'**{ctx.author.mention} поцеловал(-а) всех!...?\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
            embed.set_image(url=f'{choice(kissanime)}')
            embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if member == ctx.author and member != None:
            embed = discord.Embed(description=f'**{ctx.author.mention} поцеловал(-а) себя... всмысле, как!? (￣□￣」)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
            await ctx.send(embed=embed)
    
    @commands.command()
    async def cry(self,ctx, *, reason = None):
      embed = discord.Embed(description=f'**{ctx.author.mention} плачет! (T-T)\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
      embed.set_image(url=f'{choice(animecry)}')
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
      await ctx.send(embed=embed)
    
    @commands.command()
    async def tea(self,ctx, *, reason = None):
      embed = discord.Embed(description=f'**{ctx.author.mention} пьёт чай!\n{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
      embed.set_image(url=f'{choice(teaanime)}')
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
      await ctx.send(embed=embed)

    @commands.command()
    async def ship(self, ctx, member: discord.Member = None, member1: discord.Member = None):
            randomlov = randint(0,100)
            if member1 == None:
                embed = discord.Embed(description=f'**{ctx.author.mention} любит {member.mention} на {randomlov}% {"💞" if randomlov > 75 else ""}{"🤍" if randomlov > 50 and randomlov < 76 else ""}{"💔" if randomlov > 25 and randomlov < 51 else ""}{"💘" if randomlov > 10 and randomlov < 26 else ""}{"🖤" if randomlov > -1 and randomlov < 11 else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                await ctx.send(embed=embed)
            if member1 != None:
                embed = discord.Embed(description=f'**{member.mention} любит {member1.mention} на {randomlov}% {"💞" if randomlov > 75 else ""}{"🤍" if randomlov > 50 and randomlov < 76 else ""}{"💔" if randomlov > 25 and randomlov < 51 else ""}{"💘" if randomlov > 10 and randomlov < 26 else ""}{"🖤" if randomlov > -1 and randomlov < 11 else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(reaction(client))
    print(f"{Fore.GREEN}Cog 'reaction' load!{Fore.RESET}")