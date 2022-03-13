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

class moder(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self,ctx, amount: int):
        if ctx.author.guild_permissions.manage_messages:
            amount = int(amount)
            await ctx.channel.purge(limit = amount+1)
            emb = discord.Embed(title = "Чат был очищен", colour = discord.Color.purple())
            await ctx.send(embed=emb, delete_after=10)
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send(f'У вас прав нет!')
    
    
    
    @commands.command()
    async def kick(self, ctx, user: discord.Member = None, *, reason = None):
        if ctx.author.guild_permissions.kick_members:
            if user == None:
                embed = discord.Embed(description=f'**{ctx.author.name} вы не указали пользователя!**', color = discord.Color.from_rgb(255, 215, 0))
                await ctx.send(embed=embed)
            if user != None:
                try:
                    embed = discord.Embed(description=f'**<:1628_warn:927224619826561106> Пользователь __{user.name}#{user.discriminator}__ был кикнут с сервера!\n\n__Модератор__: __{ctx.author.name}#{ctx.author.discriminator}__\n{"__Причина:__ " if reason != None else ""}{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                    embed.set_thumbnail(url=user.avatar_url)
                    await ctx.send(embed=embed)
                    embed1 = discord.Embed(description=f'**<:1628_warn:927224619826561106> Вы были кикнуты на сервере {ctx.guild.name}!\n\n__Модератор__: __{ctx.author.name}#{ctx.author.discriminator}__\n{"__Причина:__ " if reason != None else ""}{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                    embed1.set_thumbnail(url=user.avatar_url)
                    try:
                        await user.send(embed=embed1)
                    except:
                        pass
                    await user.kick(reason=reason)
                except:
                    await ctx.send(f'Что-то пошло не так и пользователя не удалось кикнуть.')
                await ctx.message.delete()
        if not ctx.author.guild_permissions.kick_members:
            embed = discord.Embed(description=f'**{ctx.author.name} вы не можете кикать потому-что у вас недостаточно прав!**', color = discord.Color.from_rgb(255, 215, 0))
            await ctx.send(embed=embed)
    
    @commands.command()
    async def ban(self, ctx, user = None, *, reason = None):
        if ctx.author.guild_permissions.ban_members:
            if user == None:
                embed = discord.Embed(description=f'**{ctx.author.name} вы не указали пользователя!**', color = discord.Color.from_rgb(255, 215, 0))
                await ctx.send(embed=embed)
            if user != None:
                try:
                    mem = self.client.get_user(int(''.join([x for x in user if x.isdigit()])))
                    embed = discord.Embed(description=f'**<:1628_warn:927224619826561106> Пользователь __{mem.name}#{mem.discriminator}__ был забанен на сервере!\n\n__Модератор__: __{ctx.author.name}#{ctx.author.discriminator}__\n{"__Причина:__ " if reason != None else ""}{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                    embed.set_thumbnail(url=mem.avatar_url)
                    await ctx.send(embed=embed)
                    embed1 = discord.Embed(description=f'**<:1628_warn:927224619826561106> Вы были забанены на сервере {ctx.guild.name}!\n\n__Модератор__: __{ctx.author.name}#{ctx.author.discriminator}__\n{"__Причина:__ " if reason != None else ""}{reason if reason != None else ""}**', color = discord.Color.from_rgb(255, 215, 0))
                    embed1.set_thumbnail(url=mem.avatar_url)
                    try:
                        await mem.send(embed=embed1)
                    except:
                        pass
                    await ctx.guild.ban(mem,reason=reason)
                except:
                    await ctx.send(f'Что-то пошло не так и пользователя не удалось забанить.')
                await ctx.message.delete()
        if not ctx.author.guild_permissions.ban_members:
            embed = discord.Embed(description=f'**{ctx.author.name} вы не можете банить потому-что у вас недостаточно прав!**', color = discord.Color.from_rgb(255, 215, 0))
            await ctx.send(embed=embed)
    
    @commands.command()
    async def unban(self,ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')
    
      for ban_entry in banned_users:
        user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} Были успешно разбанены")
      if not ctx.author.guild_permissions.ban_members:
        await ctx.send(f'У вас прав нет!')
        return

def setup(client):
    client.add_cog(moder(client))
    print(f"{Fore.GREEN}Cog 'moder' load!{Fore.RESET}")