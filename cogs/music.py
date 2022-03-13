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

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    
        

def setup(client):
    client.add_cog(music(client))
    print(f"{Fore.GREEN}Cog 'music' load!{Fore.RESET}")