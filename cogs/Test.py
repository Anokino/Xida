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
#import Pillow
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
        print('Divers Cog : Config loaded')
    except:
        print('Divers Cog : Fail to load config')




class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))
        

    @commands.command(aliases = ["ex", "execute"])
    async def exec(self, ctx, msg):
        """Pour éxécuter du code"""

        exec(open(msg).read())

    @commands.command(name="birb")
    async def _birb(self, ctx):
        img = await self.client.random_image("birb")
        e = discord.Embed(description="Birb, demandé par {}".format(ctx.author.name), title='Avatar', color=0xF47B67, timestamp=datetime.utcnow())
        e.set_image(url=img.url)
        e.set_footer(text="Codé par Anokino#5203", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(name="tsearch", aliases=["tagsearch", "tagsh"])
    async def _isearch(self, ctx, *, tag):
        """Recherche d'image par tag
        Tags: <pepe>, <doge>, <kappa>, <dab>, <birb>, <dog>, <fbi>, <kiss>, <pat>, <hug>, <fox>, <lick>, <headrub>
        Nsfw Tags": <hentai_gif>, <neko>"""
        img = await self.client.random_image(tag)
        e = discord.Embed(description="Image demandée par {}".format(ctx.author.name), title=tag, color=0xF47B67, timestamp=datetime.utcnow())
        e.set_image(url=img.url)
        e.set_footer(text="Codé par Anokino#5203", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)

    @commands.command(name="edit")
    async def _edit(self, ctx):
        await ctx.send('lul')
        await asyncio.sleep(5)
        await self.edit(content='lol')







def setup(bot):
    bot.add_cog(Test(bot))