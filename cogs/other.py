import discord, json, requests, asyncio, os, time, keep_alive, aiohttp, io, youtube_dl, typing, pytz
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.utils import get
from discord import gateway
from random import choice, randint
from discord import Spotify
from imagelink import nekoimage, animehug, animebite, animepat, animelick, animeboop, animecry, kissanime, teaanime
from Cybernator import Paginator
from pymongo import MongoClient
from colorama import Fore
from dotenv import load_dotenv
from discord_components import *
from datetime import datetime
from discord import FFmpegPCMAudio
from googletrans import Translator
from discord_together import DiscordTogether

cluster = MongoClient(os.environ.get('MONGO'))
collection = cluster.ecodb.colldb

def get_prefix(client, message):
    if message.channel != message.author.dm_channel:
        prefix = collection.find_one({"_id": message.guild.id})["prefix"]
        return prefix
    if message.channel == message.author.dm_channel:
        prefix = ">"
        return prefix
      
message_cooldown = commands.CooldownMapping.from_cooldown(1.0, 500, commands.BucketType.user)

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


class other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bot(self, ctx):
      dpy = discord.__version__
      bot = self.client.get_user(919865860116590613)
      developer = self.client.get_user(888846101531213824)
      ping = (round(self.client.latency * 1000))
      embed = discord.Embed(description=f'`⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀о боте⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`\n\n⠀⠀⠀⠀⠀⠀__ОСНОВНОЕ__\n**<:2762roleiconbot:926837385092825118> <:3199blurplejoin:926823489275584542> Название: {bot.name}#{bot.discriminator}\n<:1312modcertified:926833509413322792> <:3199blurplejoin:926823489275584542> ID: {bot.id}\n<:4323blurpleverifiedbotdeveloper:926841430574530631> <:3199blurplejoin:926823489275584542> Создатель: {developer.name}#{developer.discriminator}**\n⠀⠀⠀⠀⠀⠀__ДРУГОЕ__\n**<:6585blurplecompass:926837384996331561> <:3199blurplejoin:926823489275584542> Задержка: {ping}ms `{"хорошая" if ping < 36 else ""}{"стабильная" if ping > 35 and ping < 46 else ""}{"плохая" if ping > 45 and ping < 101 else ""}{"хуже некуда" if ping > 100 and ping < 501 else ""}`\n<:4320_bot:926866170974470226> <:3199blurplejoin:926823489275584542> Discord.py: {dpy}\n<:4343blurpleconnection:926843343852433528> <:3199blurplejoin:926823489275584542> Серверов: {len(self.client.guilds)}\n<:8263blurplemembers:926841430574510131> <:3199blurplejoin:926823489275584542> Участников: {len(set(self.client.get_all_members()))}**', color = discord.Color.from_rgb(104, 159, 104))
          
      embed.set_thumbnail(url=bot.avatar_url)
      embed.set_footer(text=f'Все права защищены! | 2021 - 2022®',icon_url=developer.avatar_url)
          
      embed1 = discord.Embed(description=f'Я фурри дракон бот, который вам расскажет об фурри и драконах, или сделать хороший сервер. Мой хозяин, {developer.name}, заботится обо мне. Также я люблю рыбу и мясо (особенно свинину)!', color = discord.Color.from_rgb(104, 159, 104))
          
      embed1.set_thumbnail(url=bot.avatar_url)
      embed1.set_footer(text=f'Все права защищены! | 2021 - 2022®',icon_url=developer.avatar_url)
      embeds = [embed,embed1]
      
      msg = await ctx.send(embed=embed)
      reactions = ["<:9390blurpleleave:926823489330118726>","<:3199blurplejoin:926823489275584542>"]
      
      page = Paginator(self.client, message=msg,only=ctx.author,timeout=90,reactions=reactions,use_exit=True,exit_reaction=["<:3697crosspink:926830311076159538>"],delete_message=True,footer=False, embeds=embeds)
        
      await page.start()


    @commands.command(aliases = ['Ping', 'PING', 'pING', 'ping', 'Пинг', 'ПИНГ', 'пИНГ', 'пинг', 'Понг', 'ПОНГ', 'пОНГ', 'понг'])
    async def __ping(self,ctx):
        ping = self.client.latency 
    
        ping_emoji = "<:7881_battery_full:927180739689201704>"
    
        if ping > 0.10000000000000000:
            ping_emoji = "<:7431theconnectionisexcellent:927180739278172231>"
    
        if ping > 0.15000000000000000:
            ping_emoji = "<:4517_battery_half:927180739819221022>"
    
        if ping > 0.20000000000000000:
            ping_emoji = "<:3657theconnectionisgood:927180739630465044>"
    
        if ping > 0.25000000000000000:
            ping_emoji = "<:5929_battery_low:927180739554996224>"
    
        if ping > 0.30000000000000000:
            ping_emoji = "<:8920theconnectionisbad:927180739315920906>" 
    
        if ping > 0.35000000000000000:
            ping_emoji = "<:2476_battery_empty:927180739232034847>"
    
        message = await ctx.send('Пожалуйста, подождите. . .')
        await message.edit(content = f'Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:') 



    @commands.command()
    async def avatar(self,ctx, member: discord.Member = None):
        user = member or ctx.author
        embed = discord.Embed(description=f'**<:8196blurpleimage:926843343537860689> <:3199blurplejoin:926823489275584542> Аватарка {user.name}**', color = 0x7289da)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['user', 'юзер', 'profile'])
    async def __user(self,ctx, member: discord.Member = None):
          user = member or ctx.author
          t = user.status
          if t == discord.Status.online:
              d = "<:5251onlinestatus:926818256805834783>В сети"
          t = user.status
          if t == discord.Status.offline:
              d = "<:2179offlinestatus:926818256982007859> <:1656_idle:>Не в сети"
          t = user.status
          if t == discord.Status.idle:
              d = "<:5505idlestatus:926821523396886558>Не активен"
          t = user.status
          if t == discord.Status.dnd:
              d = "<:5163dndstatus:926818256906485821>Не беспокоить"
          embed = discord.Embed(description=f"`⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀профиль⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`\n**<:2899info:926833496520003584>  <:3199blurplejoin:926823489275584542> Имя: __{user.name}__\n<:3349book:926835682536718366> <:3199blurplejoin:926823489275584542> ID: __{user.id}__\n<:8917blurpleticket:926841430838763610> <:3199blurplejoin:926823489275584542> Тег: __#{user.discriminator}__\n <:3199blurplejoin:926823489275584542> Статус: __{d}__\n<:1032blurplebell:926843343533666325> <:3199blurplejoin:926823489275584542> Пользовательский статус: __{user.activity if user.activity != None else 'Отсутствует'}__\n<:6585blurplecompass:926837384996331561> <:3199blurplejoin:926823489275584542> Присоединился к серверу: {user.joined_at.year}.{user.joined_at.month}.{user.joined_at.day} {user.joined_at.hour}:{user.joined_at.minute}:{user.joined_at.second}\n<:8263blurplemembers:926841430574510131> <:3199blurplejoin:926823489275584542> Дата регистрации: {user.created_at.year}.{user.created_at.month}.{user.created_at.day}**", color=0x9b59b6)
          embed.set_thumbnail(url=user.avatar_url)
          await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx, *, msg=None):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(aliases = ['баг'])
    async def bug(self,ctx, *, msg=None, member: discord.Member = None):
      user = member or ctx.author 
      await ctx.send(f'{ctx.author.name} сообщение о баге было отправлено к тех поддержке!')
      await ctx.message.delete()
      channel = self.client.get_channel(927180606218059790)
      embed= discord.Embed(description = f"**СООБЩЕНИЕ О БАГЕ**\n{msg}", color = discord.Color.from_rgb(255, 205, 0))
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text=f'{ctx.guild.name} Участник: {ctx.author.id}',icon_url=ctx.guild.icon_url)
      await channel.send(embed=embed)

    @commands.command(aliases = ['идея'])
    async def idea(self,ctx, *, msg=None, member: discord.Member = None):
      user = member or ctx.author 
      await ctx.send(f'{ctx.author.name} сообщение о идее было отправлено к тех поддержке!')
      await ctx.message.delete()
      channel = self.client.get_channel(928674550353375332)
      embed= discord.Embed(description = f"**СООБЩЕНИЕ О ИДЕЕ**\n{msg}", color = discord.Color.from_rgb(255, 205, 0))
      embed.set_thumbnail(url=user.avatar_url)
      embed.set_footer(text=f'{ctx.guild.name} Участник: {ctx.author.id}',icon_url=ctx.guild.icon_url)
      await channel.send(embed=embed)


    @commands.command()
    async def server(self,ctx):
      categories = len(ctx.guild.categories)
      channels = len(ctx.guild.channels)
      textchannels = len(ctx.guild.text_channels)
      voicechannels = len(ctx.guild.voice_channels)
      online = sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)
      offline = sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)
      idle = online = sum(member.status==discord.Status.idle and not member.bot for member in ctx.guild.members)
      dnd = online = sum(member.status==discord.Status.dnd and not member.bot for member in ctx.guild.members)
      humans = sum(not member.bot for member in ctx.guild.members)
      bots = sum(member.bot for member in ctx.guild.members)
      roles = len(ctx.guild.roles)
      boostlevel = ctx.guild.premium_tier
      boosts = ctx.guild.premium_subscription_count
        

      embed = discord.Embed(description=f"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`ОСНОВНОЕ`\n<:2899info:926833496520003584> <:3199blurplejoin:926823489275584542> Название: {ctx.guild.name}\n<:3349book:926835682536718366> <:3199blurplejoin:926823489275584542> ID: {ctx.guild.id}\n<:6632serverowner:927142125970288660> <:3199blurplejoin:926823489275584542> Создатель: {ctx.guild.owner.name}\n<:8196blurpleimage:926843343537860689> <:3199blurplejoin:926823489275584542> Аватарка: __[ссылка]({ctx.guild.icon_url})__\n<:9407useemojis:927154708437692438> <:3199blurplejoin:926823489275584542> Создан: `в {ctx.guild.created_at.year} году {ctx.guild.created_at.day} {'Января' if ctx.guild.created_at.month == 1 else ''}{'Февраля' if ctx.guild.created_at.month == 2 else ''}{'Марта' if ctx.guild.created_at.month == 3 else ''}{'Апреля' if ctx.guild.created_at.month == 4 else ''}{'Мая' if ctx.guild.created_at.month == 5 else ''}{'Июня' if ctx.guild.created_at.month == 6 else ''}{'Июля' if ctx.guild.created_at.month == 7 else ''}{'Августа' if ctx.guild.created_at.month == 8 else ''}{'Сентября' if ctx.guild.created_at.month == 9 else ''}{'Октября' if ctx.guild.created_at.month == 10 else ''}{'Ноября' if ctx.guild.created_at.month == 11 else ''}{'Декабря' if ctx.guild.created_at.month == 12 else ''}` `{ctx.guild.created_at.hour}:{ctx.guild.created_at.minute}:{ctx.guild.created_at.second}`\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`КАНАЛЫ`\n<:7655discordcategoriesfromvega:927146265236623372> <:3199blurplejoin:926823489275584542> Категории: {categories}\n<:5702blurpletextchannel:927145219982512209> <:3199blurplejoin:926823489275584542> Текстовые: {textchannels}\n<:3527blurplevoicechannel:927145219768610878> <:3199blurplejoin:926823489275584542> Голосовые: {voicechannels}\n<:5413blurplechat:927155719504011284> <:3199blurplejoin:926823489275584542> Всего: {channels}\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`УЧАСТНИКИ`\n<:8263blurplemembers:926841430574510131> <:3199blurplejoin:926823489275584542> Всего: {ctx.guild.member_count}\n<:5251onlinestatus:926818256805834783> <:3199blurplejoin:926823489275584542> Онлайн: {online}\n<:2179offlinestatus:926818256982007859> <:3199blurplejoin:926823489275584542> Не в сети: {offline}\n<:5505idlestatus:926821523396886558> <:3199blurplejoin:926823489275584542> Неактивны: {idle}\n<:5163dndstatus:926818256906485821> <:3199blurplejoin:926823489275584542> Не беспокоить: {dnd}\n<:8263blurplemembers:926841430574510131> <:3199blurplejoin:926823489275584542> Участников: {humans}\n<:2762roleiconbot:926837385092825118> <:3199blurplejoin:926823489275584542> Ботов: {bots}\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`РОЛИ И ЭМОДЗИ`\n<:8859discordrolesfromvega:927146265295347713> <:3199blurplejoin:926823489275584542> Ролей: {roles}\n**<:9685goldsnowflake:927154708605468753> <:3199blurplejoin:926823489275584542> Эмодзи: {len(ctx.guild.emojis)}\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`БУСТЫ`\n<:3874boostwithsparkles:927154708676739112> <:3199blurplejoin:926823489275584542> Уровень: {boostlevel}\n<:5131nitroboost:927154708588683354> <:3199blurplejoin:926823489275584542> Бустов: {boosts}", color = discord.Color.from_rgb(255, 215, 0))
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.send(embed=embed)


    @commands.command()
    async def spotify(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        spot = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)

        if not spot:
            embed = discord.Embed(description=f'**{ctx.author.mention} у {"вас" if member == ctx.author else "пользователя"} должен быть статус "Слушает Spotify"! (<:7370_Spotify:926884504465989662>)**', color = 0x7289da)
            embed.set_image(url='https://media.discordapp.net/attachments/864016287164006460/923936805882064927/PicsArt_11-01-05.39.44.png?width=888&height=317')
            await ctx.send(embed=embed)
        if spot:

            embed = discord.Embed(title = f"<:7370_Spotify:926884504465989662> ･ {member} слушает Spotify!", color = spot.color)
            embed.add_field(name = "Трек", value = f'__[{spot.title}](https://open.spotify.com/track/{spot.track_id})__')
            embed.add_field(name = "Исполнитель", value = spot.artist)
            embed.add_field(name = "Альбом", value = spot.album)
            embed.add_field(name = "Длительность аудио", value = strfdelta(spot.duration, '{hours:02}:{minutes:02}:{seconds:02}'))
            embed.set_thumbnail(url = spot.album_cover_url)
            embed.set_image(url='https://media.discordapp.net/attachments/864016287164006460/923936805882064927/PicsArt_11-01-05.39.44.png?width=888&height=317')

            await ctx.send(embed = embed)


    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(os.environ.get('Token')) 
          
    @commands.command()
    async def youtube(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        embed = discord.Embed(description=f"Нажмите __[сюда]({link})__ чтобы запустить совместный просмотрYouTube!\n`Предупреждение: эта функция для пк, а в телефоне не работает`")
        await ctx.send(embed=embed)
              
def setup(client):
    client.add_cog(other(client))
    print(f"{Fore.GREEN}Cog 'other' load!{Fore.RESET}")