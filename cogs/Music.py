import discord, logging, json #importer la librairie discord.py
import colorama
import asyncio
import platform
import sys
import pylint.lint
from discord.ext.commands import Bot
from discord.ext import commands #importer des commandes spécifiques de la librairie
import os
import requests
import urllib.request
import json
import time
import random
import datetime
import traceback
from datetime import datetime
from profanity import profanity
from tinydb import TinyDB, Query
from tinydb.operations import delete,increment
from colorama import *
from random import randint
import itertools
from itertools import cycle
from colorama import Fore, Back, Style 
import logging
import ksoftapi
from pyfiglet import figlet_format, FontNotFound
from async_timeout import timeout
from functools import partial
import youtube_dl
from youtube_dl import YoutubeDL
from discord.utils import find
# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    try:
        import config  # config.py is required to run; found in the same directory.
        from config import botversion, des, pref, bbtoken, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img, slap_img, poke_img # setup.py is used to get the version number
        print('Musique Cog : Config loaded')
    except:
        print('Musique Cog : Fail to load config')


# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))
        #self.init_logger()

    #def init_logger(self):
    #    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    #    logging.basicConfig(level='DEBUG', format=FORMAT, handlers=[
    #        logging.FileHandler("logs.log"),
    #        logging.StreamHandler()
    #    ])

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Rejoint un canal vocal"""
        try:
            print('connected1')
            #if ctx.voice_client is not None:
            #    return await ctx.voice_client.move_to(channel)

            await channel.connect()
            print('connected2')
        except Exception as e:
                await ctx.send(e.args)
                print(e.args)

    @commands.command()
    async def play(self, ctx, *, query):
        """Joue un fichier à partir du local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(query))

    @commands.command()
    async def yt(self, ctx, *, url):
        """Lecture à partir d'une url (presque tout ce que youtube_dl supporte)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def stream(self, ctx, *, url):
        """Stream à partir d'une url (identique à yt, mais ne pré-télécharge pas)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Modifie le volume du son"""

        if ctx.voice_client is None:
            return await ctx.send("Non connecté à un canal vocal")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stoppe et déconnecte le bot du vocal"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Vous n'êtes pas connecté à un canal vocal.")
                raise commands.CommandError("L'auteur n'est pas connecté à un canal vocal.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

def setup(bot):
    bot.add_cog(Music(bot))
