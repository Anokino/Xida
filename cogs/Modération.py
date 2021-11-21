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
        print('Modération Cog : Config loaded')
    except:
        print('Modération Cog : Fail to load config')



class Modération(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot = self.bot
        self._last_member = None
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))


    @commands.command(aliases=['sy'])
    async def say(self, ctx, *, texte):
        """Pour faire dire quelque chose au Bot"""
        await ctx.message.delete()
        await ctx.send(texte)

    @commands.command(aliases=['em'])
    async def embed(self, ctx, embed_type_en_un_seul_mot, *, texte):
        """Créer un embed"""
        await ctx.message.delete()
        e = discord.Embed(color=0xff1117, timestamp=datetime.utcnow())
        e.add_field(name=embed_type_en_un_seul_mot, value=texte)
        e.set_footer(text=f'Xida, demandé par : {ctx.author.name}')
        await ctx.send(embed=e)

    @commands.command(aliases = ["sdg"])
    async def sondage(self, ctx, sondage):
        """Pour créer un sondage"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
        e.add_field(name=f'Sondage : *``Demandé par {ctx.author.name}``*', value=f'{sondage}')
        e.set_footer(text=f'Réagissez avec les réactions ci-dessous pour donner votre avis !')
        m = await ctx.send(embed=e)
        asyncio.sleep(0.3)
        await m.add_reaction(emoji="✅")
        asyncio.sleep(0.2)
        await m.add_reaction(emoji="❌")

    @commands.has_permissions(kick_members=True)
    @commands.command(name="osub", aliases = ["osug", " ouisuggestion", "sugo", "suggestionoui", "subo"])
    async def _osub(self, ctx, member: discord.Member, *, commentaire = None):
        """Pour accepter une suggestion"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        if commentaire is None:
            e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/423902499209084928/586637217477427261/sign-check-icon.png")
            e.add_field(name=f'Réponse de {ctx.author.name} :', value=f"{member.mention}, **ta demande a été acceptée !**")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            m = await ctx.send(embed=e)
        else:
            e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/423902499209084928/586637217477427261/sign-check-icon.png")
            e.add_field(name=f'Réponse de {ctx.author.name} :', value=f"{member.mention}, **ta demande a été acceptée !**")
            e.add_field(name=f"Commentaire : ", value=f"{commentaire}", inline=False)
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            m = await ctx.send(embed=e)


    @commands.has_permissions(kick_members=True)
    @commands.command(name="nsub", aliases = ["nsug", "nonsuggestion", "subn", "sugn", "suggestionnon"])
    async def _nsub(self, ctx, member: discord.Member, *, commentaire = None):
        """Pour décliner une suggestion"""
        await ctx.message.delete()
        asyncio.sleep(0.2)
        if commentaire is None:
            e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/423902499209084928/586637363409584130/xx.png")
            e.add_field(name=f'Réponse de {ctx.author.name} :', value=f"{member.mention}, **ta demande a été declinée x(**")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            m = await ctx.send(embed=e)
        else:
            e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/423902499209084928/586637363409584130/xx.png")
            e.add_field(name=f'Réponse de {ctx.author.name} :', value=f"{member.mention}, **ta demande a été declinée x(**")
            e.add_field(name=f"Commentaire : ", value=f"{commentaire}", inline=False)
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            m = await ctx.send(embed=e)

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def clear(self, ctx, nombre_de_messages : int):
        """Pour effacer des messages"""
        await ctx.message.delete()
        await ctx.channel.purge(limit=nombre_de_messages)
        await ctx.send(f"J'ai supprimé **{nombre_de_messages}** messages")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        """Chut jeune padawan"""
        await ctx.message.delete()
        try:
            await bot.add_roles(*539485500042510357, reason=None, atomic=True)
            await ctx.send('{} a bien été muté !'.format(member))

        except:

            e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name="**Permissions Insuffisantes**", value="­­ ")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)


    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def kick(self, ctx, member: discord.Member, *, raison):
        """Quelqu'un fait des bêtises ?"""
        await ctx.message.delete()
        try:
            e = discord.Embed(title="__**Kick de Membre**__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name='{} a bien été exclu !'.format(member), value=f'avec comme raison : {raison}')
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)
            await member.kick()

        except:
            e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name="**Permissions Insuffisantes**", value="­­ ")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)



    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, raison):
        """Ca n'inspire rien de bon en général"""
        await ctx.message.delete()
        try:
            e = discord.Embed(title="__**Ban de Membre**__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name='{} a bien été banni !'.format(member), value=f'avec comme raison : {raison}')
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)
            await member.ban()

        except:
            e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name="**Permissions Insuffisantes**", value="­­ ")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)


    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, member: discord.Member):
        """Quelqu'un à débannir ?"""
        await ctx.message.delete()
        try:
            e = discord.Embed(title="__**>Unban de Membre**__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name='{} a bien été débanni !'.format(member), value=f'✅')
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)
            await member.unban()

        except:
            e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
            e.add_field(name="**Permissions Insuffisantes**", value="­­ ")
            e.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=e)

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def getbans(self, ctx):
        """Liste tous les utilisateurs bannis sur le serveur actuel."""

        #for cog in self.bot.cogs: CECI CREER UNE LISTE (a adpater)
        #    e.add_field(name='Nombre actuel de commandes', value=str(len(self.bot.get_cog(cog).get_commands())))

        try:
            bans = await ctx.guild.bans()

            for ban in bans:
                raisonban = ban.reason
                #await ctx.send(bans)
                if raisonban == 'Unspecified.':
                    raisonban = 'Non spécifiée'
                    await ctx.send(f'**Bannissement :** {ban.user} **ID :** {ban.user.id} **|** **Raison :** {raisonban} ')
                else:
                    await ctx.send(f'**Bannissement :** {ban.user} **ID :** {ban.user.id} **|** **Raison :** {raisonban} ')
                    #embed=discord.Embed(title="Banissements", description=f"Serveur : {ctx.guild}", color=0xce0005, timestamp=datetime.utcnow())
                    #embed.set_thumbnail(url = ctx.guild.icon_url)
                    #embed.set_footer(text="Codé par Anokino#5203", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
                    #await ctx.send(embed=embed)
                    #await ctx.send(f'Bannissements : {ban.user} , {raisonban} ')

        except:
            await ctx.send(config.err_mesg)
            await ctx.message.add_reaction(emoji="❗")

    # TODO: Add reason with ban
    @commands.command(aliases=['hban'], pass_context=True)
    async def hackban(self, ctx, guild, user_id: int):
        """Bans a user outside of the server."""
        #author = ctx.message.author
        guild.id = ctx.guild.id

        user = guild.get_member(user_id)
        if user is not None:
            return await ctx.invoke(self.ban, user=user)

        try:
            await self.bot.http.ban(user_id, guild.id, 0)
            await ctx.message.edit(content=self.bot.bot_prefix + 'Banned user: %s' % user_id)
        except discord.NotFound:
            await ctx.message.edit(content=self.bot.bot_prefix + 'Could not find user. '
                               'Invalid user ID was provided.')
        except discord.errors.Forbidden:
            await ctx.message.edit(content=self.bot.bot_prefix + 'Could not ban user. Not enough permissions.')




def setup(bot):
    bot.add_cog(Modération(bot))
