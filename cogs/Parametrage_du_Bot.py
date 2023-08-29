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
        from config import nombot, createur, botversion, des, pref, bbtoken, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img, slap_img, poke_img # setup.py is used to get the version number
        print('Parametrage_du_Bot Cog : Config loaded')
    except:
        print('Parametrage_du_Bot Cog : Fail to load config')



class Parametrage_du_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))


    @commands.command(pass_context = True)
    async def rpdef(self, ctx):
        """Remet le statut par défault - **Désactivé**"""
        #if ctx.author.id == 305066808660983811 :
        #    e = discord.Embed(title="Bot en mode \"Online\" pour:", description="Raison par défault", color=0x16c06b, timestamp=datetime.utcnow())
        #    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
        #    e.add_field(name='(Défault :)', value=f"({default_rich_presence})")
        #    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
        #    await ctx.send(embed=e)
        #    await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=default_rich_presence))
        #if ctx.author.id == 386458437409570816 :
        #    e = discord.Embed(title="Bot en mode \"Online\" pour:", description="Raison par défault", color=0x16c06b, timestamp=datetime.utcnow())
        #    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
        #    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
        #    await ctx.send(embed=e)
        #    await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=default_rich_presence))
        await ctx.message.add_reaction("⚠")
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Désactivée")

    @commands.command(pass_context = True, aliases=['on', 'ONLINE', 'onl', 'On'])
    async def rponline(self, ctx, *, texte):
        """Statut En Ligne - **Désactivé**"""
        #if ctx.author.id == 305066808660983811 :
        #    e = discord.Embed(title="Bot en mode \"Online\" pour:", description=texte, color=0x16c06b, timestamp=datetime.utcnow())
        #    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
        #    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
        #    await ctx.send(embed=e)
        #    await ctx.change_presence(status=discord.Status.online, activity=discord.Game(name=texte))
        #if ctx.author.id == 386458437409570816 :
        #    e = discord.Embed(title="Bot en mode \"Online\" pour:", description=texte, color=0x16c06b, timestamp=datetime.utcnow())
        #    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
        #    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
        #    await ctx.send(embed=e)
        #    await ctx.change_presence(status=discord.Status.online, activity=discord.Game(name=texte))
        await ctx.message.add_reaction("⚠")
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Désactivée")

    @commands.command(pass_context = True, aliases=['in', 'IDLE', 'idl', 'IN'])
    async def rpidle(self, ctx, *, texte):
        """Statut inactif - **Désactivé**"""
    #    if ctx.author.id == 305066808660983811 :
    #        e = discord.Embed(title="Bot en mode \"Inactif\" pour:", description=texte, color=0xd9a904, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=texte))
    #    if ctx.author.id == 386458437409570816 :
    #        e = discord.Embed(title="Bot en mode \"Inactif\" pour:", description=texte, color=0xd9a904, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=texte))
        await ctx.message.add_reaction("⚠")
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Désactivée")

    @commands.command(pass_context = True)
    async def rpdnd(self, ctx, *, texte):
        """Statut Ne pas déranger - **Désactivé**"""
    #    if ctx.author.id == 305066808660983811 :
    #        e = discord.Embed(title="Bot en \"Ne pas déranger\" pour:", description=texte, color=0xcc3939, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=texte))
    #    if ctx.author.id == 386458437409570816 :
    #        e = discord.Embed(title="Bot en \"Ne pas déranger\" pour:", description=texte, color=0xcc3939, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=texte))
        await ctx.message.add_reaction("⚠")
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Désactivée")

    @commands.command(pass_context = True, aliases=['st', 'str', 'ST'])
    async def rpstream(self, ctx, *, texte):
        """Statut stream - **Désactivé**"""
    #    if ctx.author.id == 305066808660983811 :
    #        e = discord.Embed(title="Bot en mode \"Online\" pour:", description=texte, color=0x16c06b, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.streaming, activity=discord.Game(name=texte))
    #    if ctx.author.id == 386458437409570816 :
    #        e = discord.Embed(title="Bot en mode \"Online\" pour:", description=texte, color=0x16c06b, timestamp=datetime.utcnow())
    #        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
    #        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
    #        await ctx.send(embed=e)
    #        await ctx.bot.change_presence(status=discord.Status.streaming, activity=discord.Game(name=texte))
        await ctx.message.add_reaction("⚠")
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Désactivée")


async def setup(bot):
    await bot.add_cog(Parametrage_du_Bot(bot))