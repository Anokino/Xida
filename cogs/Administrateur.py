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
        from config import cogs, botversion, des, pref, bbtoken, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img, slap_img, poke_img # setup.py is used to get the version number
        print('Administrateur Cog : Config loaded')
    except:
        print('Administrateur Cog : Fail to load config')

class Administrateur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))



    @commands.command()
    async def exsay(self, ctx, guildid: discord.Guild, channel: discord.TextChannel, *, texte):
        """say for admin"""
        if ctx.author.id == 305066808660983811 :
            try:
                my_guild = self.bot.get_guild(guildid)
                await asyncio.sleep(0.5)
                chnl_sd = my_guild.get_channel(channel)
                await chnl_sd.send(texte)
            except Exception as e:
                await ctx.send(e.args)
                print(e.args)
        else:
            await ctx.send(" :x: Désolé mais seul l'administrateur peut éxécuter cette commande.")

    @commands.command()
    async def leaveserv(self, ctx, idnum):
        if ctx.author.id == 305066808660983811 :
            try:
                idnum = self.bot.get_guild(idnum)
                await idnum.leave()
                await ctx.send(f'Server {idnum.name} left.')
            except Exception as e:
                await ctx.send(e.args)
                print(e.args)
        else:
            await ctx.send(" :x: Désolé mais seul l'administrateur peut éxécuter cette commande.")


    @commands.command(pass_context = True)
    async def restart(self, ctx):
        """Relance le Bot (utile en cas de problème)"""
        if ctx.author.id == 305066808660983811 :
            await ctx.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='Redémarrage...'))
            e = discord.Embed(title="Redémarrage", description="Xina", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://www.rogers.com/web/smb/bss/images/widget-loader-lg_no-lang.gif")
            e.add_field(name='Bot:', value='Chargement...')
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=2)

            e = discord.Embed(title="Redémarrage", description="Xina", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://www.rogers.com/web/smb/bss/images/widget-loader-lg_no-lang.gif")
            e.add_field(name='Bot:', value=f'Ouverture des cogs...')
            e.set_footer(text="Veuillez patienter")
            await ctx.send(embed=e)
            try:
                for cog in cogs:
                    self.bot.unload_extension(f'cogs.{cog}')
                    self.bot.load_extension(f'cogs.{cog}')
            except Exception as e:
                await ctx.send('Erreur')#\N{PISTOL}')
                await ctx.send('{}: {}'.format(type(e).__name__, e))
            else:
                await ctx.send('Ok')#\N{OK HAND SIGN}')
            await asyncio.sleep(4)
            await ctx.channel.purge(limit=1)

            e = discord.Embed(title="Redémarrage", description="Xina", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://www.rogers.com/web/smb/bss/images/widget-loader-lg_no-lang.gif")
            e.add_field(name='Bot:', value=f'Contact de l\'API Discord...')
            e.set_footer(text="Veuillez patienter")
            await ctx.send(embed=e)

            await ctx.bot.logout()
            await asyncio.sleep(2)
            self.bot.run(self.bot.run(os.environ['TOKEN']))
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=1)

            await ctx.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=default_rich_presence))
            e = discord.Embed(title="Bot redémarré !", description="Xina", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://png.pngtree.com/svg/20170315/5d8f7e389c.png")
            e.add_field(name='Bot:', value=f'Redémaré par : {ctx.author.name}')
            e.set_footer(text="Le bot peut mettre quelque temps avant de répondre.")
            await ctx.send(embed=e)
            await asyncio.sleep(3)
        else:
            await ctx.send(" :x: Désolé mais seul l'administrateur peut éxécuter cette commande.")




    @commands.command(pass_context = True)
    async def logout(self, ctx):
        """Eteint et deconnecte le Bot"""
        if ctx.author.id == 305066808660983811 :
            e = discord.Embed(title="Extinction", description="Xina", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://www.rogers.com/web/smb/bss/images/widget-loader-lg_no-lang.gif")
            e.add_field(name='Bot:', value='En cours d\'arret...')
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)
            await asyncio.sleep(12)
            await ctx.channel.purge(limit=2)
            #await ctx.send('```Cette commande est indisponible car elle provoque des instabilitées```')
            e = discord.Embed(title="Bot arrêté", description="Xina", color=0xf20000, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://png.pngtree.com/svg/20170217/toggle_off_962765.png")
            e.add_field(name='Bot:', value=f'Arrêté par : {ctx.author.name}')
            e.set_footer(text="Le bot peut apparaître toujours connecté le temps qu'une réponse soit reçue par l'api Discord, mais il est éteint.")
            await ctx.send(embed=e)
            await ctx.bot.logout()
            sys.exit
        else:
            await ctx.send(" :x: Désolé mais seul l'administrateur peut éxécuter cette commande.")

def setup(bot):
    bot.add_cog(Administrateur(bot))