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
import dbl
from dbl import *
import aiohttp

# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    try:
        import config  # config.py is required to run; found in the same directory.
        from config import nombot, createur, botversion, des, pref, bbtoken, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img, slap_img, poke_img # setup.py is used to get the version number
        print('Fun Cog : Config loaded')
    except:
        print('Fun Cog : Fail to load config')

#def setup(bot):
#    bot.add_cog(DiscordBotsOrgAPI(bot))
    
#class DiscordBotsOrgAPI:
#    	def __init__(self, bot):
#            self.bot = bot
#            self.token = os.environ['TOKEN']
#            self.dblpy = dbl.Client(self.bot, self.token)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.client = ksoftapi.Client(api_key='b9c61dbc2a0f60dbc85aa5449a4110e8cd813626')

    @commands.command()
    async def dice(self, ctx, nombre1: int = None, nombre2: int = None):
        """Tire un nombre and 'roll the dices x)'"""
        try:
            if nombre1 is None:
                nombre1 = 1
                nombre2 = 6
                rnd = randint(nombre1, nombre2)
                e = discord.Embed(description=f'(entre {nombre1} et {nombre2})', title="Lancé de dé", color=0xffffff, timestamp=datetime.utcnow())
                e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value=rnd)
                e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                await ctx.send(embed=e)
            elif nombre2 is None:
                try:
                    rnd = randint(1, nombre1)
                    e = discord.Embed(description=f'(entre 1 et {nombre1})', title="Lancé de dé", color=0xffffff, timestamp=datetime.utcnow())
                    e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                    e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value=rnd)
                    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                    await ctx.send(embed=e)
                except:
                    rnd = randint(nombre1, 1)
                    e = discord.Embed(description=f'(entre 1 et {nombre1})', title="Lancé de dé", color=0xffffff, timestamp=datetime.utcnow())
                    e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                    e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value=rnd)
                    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                    await ctx.send(embed=e)
            else:
                try:
                    rnd = randint(nombre1, nombre2)
                    e = discord.Embed(description=f'(entre {nombre1} et {nombre2})', title="Lancé de dé", color=0xffffff, timestamp=datetime.utcnow())
                    e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                    e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value=rnd)
                    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                    await ctx.send(embed=e)
                except:
                    rnd = randint(nombre2, nombre1)
                    e = discord.Embed(description=f'(entre {nombre1} et {nombre2})', title="Lancé de dé", color=0xffffff, timestamp=datetime.utcnow())
                    e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                    e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value=rnd)
                    e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                    await ctx.send(embed=e)


        except:
            await ctx.send(config.err_mesg)
            await ctx.message.add_reaction("❗")

    @commands.command()
    async def piece(self, ctx):
        """Tire une pièce à pile ou face" """
        try:
            rnd = randint(1, 2)
            if rnd ==(1):
                e = discord.Embed(description=f'Pile ou face ?', title="Lancé de pièce", color=0xffffff, timestamp=datetime.utcnow())
                e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value="Pile")
                e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                await ctx.send(embed=e)
            else:
                e = discord.Embed(description=f'Pile ou face ?', title="Lancé de pièce", color=0xffffff, timestamp=datetime.utcnow())
                e.set_thumbnail(url='https://i.imgur.com/z3kHWnZ.png')
                e.add_field(name=f"{ctx.author.name}, Voila ma réponse: ", value="Face")
                e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
                await ctx.send(embed=e)

        except:
            await ctx.send(config.err_mesg)
            await ctx.message.add_reaction("❗")

    @commands.command(name="8ball", aliases=['ball8'])
    async def _8ball(self, ctx, *, question):
        """Posez votre question, le bot vous donnera son avis 😉"""
        e = discord.Embed(title=f'8 Ball', color=(dec), timestamp=datetime.utcnow())
        e.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Magic_eight_ball.png")
        e.add_field(name=f'Question : {question}', value =f'Ma réponse: {random.choice(config.heightballp)}')
        e.set_footer(text=f'Demandé par {ctx.author.name}')
        await ctx.send(embed=e)

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        """En dévellopement"""
        try:
            url = await http.get(f'http://api.urbandictionary.com/v0/define?term={search}', res_method="json")

            if url is None:
                return await ctx.send("I think the API broke...")

            count = len(url['list'])
            if count == 0:
                return await ctx.send("Couldn't find your search in the dictionary...")
            result = url['list'][random.randint(0, count - 1)]
            
            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'
            
            embed = discord.Embed(colour=0xC29FAF, description=f"**{result['word']}**\n*by: {result['author']}*")
            embed.add_field(name='Definition', value=definition, inline=False)
            embed.add_field(name='Example', value=result['example'], inline=False)
            embed.set_footer(text=f"👍 {result['thumbs_up']} | 👎 {result['thumbs_down']}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e.args)
            print(e.args)

    @commands.command(aliases=['pf'])
    async def pokefusion(self, ctx):
        """Fusion aléatoire de pokémons"""
        poke1 = random.randrange(1, 151)
        poke2 = random.randrange(1, 151)
        
        embed = discord.Embed(title="WHO'S THAT POKEMON⁉️ :eyes:", colour=ctx.author.colour)
        embed.set_image(url=f"https://images.alexonsager.net/pokemon/fused/{poke1}/{poke1}.{poke2}.png")
        embed.set_footer(text= f"https://pokemon.alexonsager.net/{poke2}/{poke1}")
        
        await ctx.send(embed=embed)

    @commands.command(aliases=['chat_i'])
    async def chat_img(self, ctx):
        """Une photo d'un chat, parce que c'est mignon"""
        e = discord.Embed(description="Vive les chats", title='Miaou', color=0xF47B67, timestamp=datetime.utcnow())
        e.set_image(url='https://www.assuropoil.fr/wp-content/uploads/chat-heureux-en-appartement-savoir.jpg ')
        e.set_footer(text="Codé par " + createur, icon_url=(await self.bot.fetch_user('305066808660983811')).avatar)
        await ctx.send(embed=e)

    @commands.command()
    async def pat(self, ctx, *, member: discord.Member = None):
        """*Pat Pat Pat* ^o^"""
        img = await self.client.random_image("pat")
        if member is None:
            e = discord.Embed(title=f'Pat de {ctx.author.name} ┌ ^-^ ┘ ', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'{ctx.author.name} Pat {member} ^^', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)

    @commands.command(aliases=["hr", "headr", "hrub"])
    async def headrub(self, ctx, *, member: discord.Member = None):
        """Un massage crânien ? 😄"""
        img = await self.client.random_image("headrub")
        if member is None:
            e = discord.Embed(title=f'Massage de {ctx.author.name} ┌ ^-^ ┘ ', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'{ctx.author.name} masse {member} ^^', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)

    @commands.command()
    async def hug(self, ctx, *, member: discord.Member = None):
        """Faites un calin à quelqu'un"""
        img = await self.client.random_image("hug")
        if member is None:
            e = discord.Embed(title=f'Calin de {ctx.author.name}', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'Calin de {ctx.author.name} à {member}', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)

    @commands.command()
    async def kiss(self, ctx, *, member: discord.Member = None):
        """Faites un bisous à quelqu'un"""
        img = await self.client.random_image("kiss")
        if member is None:
            e = discord.Embed(title=f'Bisou de {ctx.author.name}', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title=f'Bisou de {ctx.author.name} à {member}', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=img.url)
            e.set_footer(text=f'Demandé par {ctx.author.name}')
            await ctx.send(embed=e)

    @commands.command()
    async def dab(self, ctx, *, member: discord.Member):
        """Faites un DAB 🔥"""
        img = await self.client.random_image("dab")

        e = discord.Embed(title=f'Dab de {ctx.author.name}', color=0xF47B67, timestamp=datetime.utcnow())
        e.set_image(url=img.url)
        e.set_footer(text=f'Demandé par {ctx.author.name}')
        await ctx.send(embed=e)




    @commands.command()
    async def ami(self, ctx, member: discord.Member):
        """Calcule le pourcentage de chance d'être bon ami avec quelq'un"""
        rnd = randint(0, 100)
        await ctx.send(f'{ctx.author.name}, tu as {rnd}% d\'être un bon ami avec {member.name}')

    @commands.command()
    async def cookie(self, ctx):
        """Mettez un peu de cookies dans votre vie 🍪"""
        await ctx.message.add_reaction("🍪")

async def setup(bot):
    await bot.add_cog(Fun(bot))