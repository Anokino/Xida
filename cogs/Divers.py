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



class Divers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))

    @commands.command(aliases = ["sug", "suggestion"])
    async def sub(self, ctx, sujet, plateforme, *, suggestion):
        """Pour faire une suggestion"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
        e.add_field(name=f'{sujet} -- {plateforme} -- Demandé par {ctx.author.name} ', value=suggestion)
        e.set_footer(text=f'Réagissez avec les réactions ci-dessous pour donner votre avis sur cette suggestion !')
        m = await ctx.send(embed=e)
        asyncio.sleep(0.3)
        await m.add_reaction(emoji="✅")
        asyncio.sleep(0.2)
        await m.add_reaction(emoji="❌")

    @commands.command(aliases = ["bugreport"])
    async def bug(self, ctx, sujet, plateforme, *, bug):
        """Pour faire une suggestion"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
        e.add_field(name=f'{sujet} -- {plateforme} -- Demandé par {ctx.author.name} ', value=bug)
        e.set_footer(text=f'Réagissez avec les réactions ci-dessous si vous avez aussi ce bug !')
        m = await ctx.send(embed=e)
        asyncio.sleep(0.3)
        await m.add_reaction(emoji="✅")
        asyncio.sleep(0.2)
        await m.add_reaction(emoji="❌")

    @commands.command(aliases = ["reporte"])
    async def report(self, ctx, membre: discord.Member, *, raison):
        """Si vous voulez faire un report c'est ici"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
        e.add_field(name='Report de :', value=membre)
        e.add_field(name='Raison :', value=raison)
        e.set_footer(text=f'Demandé par {ctx.author.name}:')
        m = await ctx.send(embed=e)
        asyncio.sleep(0.3)
        await m.add_reaction(emoji="✅")
        asyncio.sleep(0.2)
        await m.add_reaction(emoji="❌")


    @commands.command(aliases=["fancy"])
    async def fancify(self, ctx, *, texte):
        """Rend le texte fantaisiste !"""
        await ctx.message.delete()
        try:

            def strip_non_ascii(string):
                """Returns the string without non ASCII characters."""
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)

            text = strip_non_ascii(texte)
            if len(text.strip()) < 1:
                return await self.ctx.send(":x: ASCII characters only please!")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await ctx.send(output)

        except:
            await ctx.message.delete()
            await asyncio.sleep(0.6)
            e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name="**Erreur**", value="*Message trop long ?* ou si erreur, faites -report")
            e.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)


    @commands.command()
    async def bigtext(self, ctx, *, text):
        """Agrandit le texte."""
        await ctx.message.delete()
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="big") + "```")
        except:
            await ctx.send(config.err_mesg_t)

    @commands.command()
    async def revtext(self, ctx, *, text):
        """Met le texte à l'envers."""
        await ctx.message.delete()
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="rev") + "```")
        except:
            await ctx.send(config.err_mesg_t)

    @commands.command()
    async def text3d(self, ctx, *, text):
        """Créez du texte en 3D !"""
        await ctx.message.delete()
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="isometric1") + "```")
        except:
            await ctx.send(config.err_mesg_t)

    @commands.command()
    async def tickstext(self, ctx, *, text):
        """Des montagnes de texte"""
        await ctx.message.delete()
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="ticks") + "```")
        except:
            await ctx.send(config.err_mesg_t)

    @commands.command(aliases=['binary'])
    async def binarytext(self, ctx, *, text):
        """0110100, parlez en binaire !"""
        await ctx.message.delete()
        try:
            await ctx.send("```fix\n" + figlet_format(text, font="binary") + "```")
        except:
            await ctx.send(config.err_mesg_t)


    @commands.command()
    async def add(self, ctx, nombre1: int, nombre2: int):
        """Pour Faire une addition"""
        await ctx.send(nombre1+nombre2)

    @commands.command()
    async def min(self, ctx, nombre1: int, nombre2: int):
        """Pour faire une soustraction"""
        await ctx.send(nombre1-nombre2)

    @commands.command()
    async def mult(self, ctx, nombre1: int, nombre2: int):
        """Pour faire une multiplication"""
        await ctx.send(nombre1*nombre2)

    @commands.command()
    async def div(self, ctx, nombre1: int, nombre2: int):
        """Pour faire une division"""
        await ctx.send(nombre1/nombre2)

    @commands.command()
    async def pillow(self, ctx):
        await ctx.send('pillow')

def setup(bot):
    bot.add_cog(Divers(bot))