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
import appcommands

#from mcsrvstat import ServerStatus

# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    try:
        import config  # config.py is required to run; found in the same directory.
        from config import botversion, des, pref, bbtoken, lignes, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img, slap_img, poke_img # setup.py is used to get the version number
        print('Info Cog : Config loaded')
    except:
        print('Info Cog : Fail to load config')



class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        #self.client = ksoftapi.Client(api_key=(os.environ['APIKEY']))
        bot = appcommands.Bot(command_prefix="$")


    @commands.command(name="help", aliases=['h'])
    async def _help(self, ctx, command_name=None):
            """Affiche ce message ❔"""

            if command_name is not None:
                #await ctx.send('Erreur')
                #await ctx.send("AttributeError: 'NoneType' object has no attribute 'cog'")
                #await ctx.invoke((command_name), self.bot.get_command("usage"))
                #await ctx.send(self.bot.get_command("usage"))
                #command=command_name
                #em = discord.Embed(colour=dec)
                #em.set_author(name="Aide de " + self.bot.user.name + ":", icon_url=self.bot.user.avatar_url)
                #em.set_footer(text="Codé par Δnokino#7477",
                #            icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
                #em.add_field(name=command_name, value=self.bot.get_command("usage"))
                #await ctx.send(embed=em)

                #await ctx.invoke(self.bot.get_command("usage"), command_name)
                #await ctx.send(self.bot.get_command("usage"), command_name)
                #em = discord.Embed(colour=dec)
                #em.set_author(name="Aide de " + self.bot.user.name + ":", icon_url=self.bot.user.avatar_url)
                #em.set_footer(text="Codé par Δnokino#7477",
                #            icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
                #em.add_field(name=command_name, value=self.bot.get_command("usage"))
                #await ctx.send(embed=em)
                command= self.bot.get_command(command_name)
                parent = command.full_parent_name
                if len(command.aliases) > 0:
                    aliases = ' | '.join(command.aliases)
                    fmt = '[%s | %s]' % (command.name, aliases)
                    if parent:
                        fmt = parent + ' ' + fmt
                    alias = fmt
                else:
                    alias = command.name if not parent else parent + ' ' + command.name

                e = discord.Embed(colour=dec)
                e.add_field(name='Usage : -%s %s' % (command.name, command.signature if command.signature is not None else "No description"), value=" - " + (command.help if command.help is not None else "No description") + "\n - Alias : " + alias)
                await ctx.message.add_reaction(emoji="❔")
                return await ctx.send(embed=e)

            else:
                em = discord.Embed(colour=dec)
                em.set_author(name="Aide de " + self.bot.user.name + ":", icon_url=self.bot.user.avatar_url)
                em.set_footer(text="Codé par Δnokino#7477",
                            icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
                for cog in self.bot.cogs:
                    help_message = ""
                    for commnd in self.bot.get_cog(cog).get_commands():
                        help_message += "\n - " + commnd.name + " : " + str(commnd.help)
                    if help_message == "":
                        continue
                    else:
                        em.add_field(name=cog.replace('_', ' '), value=help_message + "\n", inline=False)
                await ctx.send(embed=em)





    @bot.usercommand(name="id")
    async def uid(ctx, user):
        await ctx.send(f"The id of {user.mention} is {user.id}", ephemeral=True)

    @bot.messagecommand(name="id")
    async def mid(ctx, msg):
        await ctx.send(f"The id of that message is {msg.id}", ephemeral=True)

    #@commands.command()
    #async def test(self, ctx):
    #    """Indique si le Bot est opérationnel ou pas"""
    #    embed = discord.Embed(color = (dec))
    #    embed.set_thumbnail(url = "https://i.imgur.com/OYubpvf.gif")
    #    embed.add_field(name="Status:", value="**🔺Le bot est actuellement en maintenance🔺**", inline=True)
    #    embed.add_field(name="Error:", value="```Certaines commandes sont innacessibles et des bugs peuvent survenir```", inline=True)
    #    embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
    #    await ctx.send(embed=embed)

    @commands.command(aliases=['te'])
    async def test(self, ctx):
        """Indique si le Bot est opérationnel ou pas"""
        embed = discord.Embed(color = (dec))
        embed.set_thumbnail(url = "http://www.etme.com/assets/loader.gif")
        embed.add_field(name="Status:", value="**Le bot est connecté et opérationnel **", inline=True)
        embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['mcstatut', 'stu', 'mcstu'])
    async def statut(self, ctx, *, ip):
            """Indique le statut d'un serveur minecraft"""
            # Ok, we are going to start here
            print("Executing command: {0}".format(f'statut {ip}'))
            await ctx.send("Ok, Veuillez patienter :D")
            # Fetch status

            try:
                status = ServerStatus(ip)
            except:# Exception as e:
                await ctx.send(":x: Désolé, mais ce serveur minecraft est down :c")
                print("Failed to find server: {0}")#.format(e))
                return

            # And the best part - send response!
            # Try sending image first
            try:
                await ctx.send(file=discord.File(status.generate_status_image()))
                return
            except Exception as err:
                print(err)
            # If sending images fails, send text message
            response = "Players online: {0} \\ {1}\nMOTD: {2}\nVersion: {3}"
            formatted_response = response.format(status.online_players, status.max_players, status.motd, status.version)

            await ctx.send("Here we go!")
            print("Response:\n{0}".format(formatted_response))
            await ctx.send(formatted_response)
            status.generate_status_image()


    #@commands.command()
       #async def test(self, ctx):
    #    """Indique si le Bot est opérationnel ou pas"""
    #    embed = discord.Embed(color = (dec))
    #    embed.set_thumbnail(url = "https://media.giphy.com/media/5kzB8SARBWCmQ/giphy.gif")
    #    embed.add_field(name="Status:", value="**❌Le bot est actuellement Down❌**", inline=True)
    #    embed.add_field(name="Error:", value="```x.ctx.bot(dynos does not respond), self.down.hbrg_error)```", inline=True)
    #    embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
    #    await ctx.send(embed=embed)


    @commands.command(aliases=['bi', 'binfo'])
    async def botinfo(self, ctx):
        """Affiche des Infos sur le Bot"""
        e = discord.Embed(title="Xina", description="C'est moi !", color=0xeccd1c, timestamp=datetime.utcnow())
        e.set_thumbnail(url=(await self.bot.fetch_user('552566569729916958')).avatar_url)
        e.add_field(name='Version', value=botversion)
        e.add_field(name='Librairie', value='Discord.py')
        e.add_field(name='Discord.py API version:', value=discord.__version__)
        e.add_field(name='OS', value=f'{platform.system()}, {platform.release()}, {"(" + os.name + ")"}')
        e.add_field(name='Python version:', value=platform.python_version())
        e.add_field(name='ID :', value="552566569729916958")
        e.add_field(name='Créateur', value='Anokino')
        e.add_field(name='Utilisateurs', value=len(ctx.bot.users))
        e.add_field(name='Invite', value=(os.environ['invite']))
        e.add_field(name='Discord', value='~~https://discord.gg/~~')
        e.add_field(name='Date version finale 1', value='Au cours de l\'année 2019')
        e.add_field(name='Nombre de lignes', value=lignes)
        cmmd_nb = str(len(self.bot.commands))

        e.add_field(name='Nombre actuel de commandes', value=cmmd_nb)
        e.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
        await ctx.send(embed=e)

    @commands.command(aliases=['pi'])
    async def ping(self, ctx): #nom de la commande
        """Renvoie le temps de latence du bot""" #description de la commande (affichée dans le message d'aide)
        await ctx.send("**Pong !**") #réponse du bot
        # Get the latency of the bot
        latency = ctx.bot.latency  # Included in the Discord.py library
        # Send it to the user
        await ctx.send(f'`Latence : {latency}`')


    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        """Inviter le Bot dans votre serveur"""
        await ctx.send("**Tu peux m'inviter grâce à ce lien :**") #lien d' invitation : https://goo.gl/nghwNo
        await ctx.send((os.environ['invite']))

    @commands.command(pass_context=True, aliases=["invitelink", "serverlink", "link"])
    async def servinvite(self, ctx):
        """*En dévellopement*"""
        invitelinknew = await self.bot.invite_create(destination = ctx.message.channel, xkcd = True, max_uses = 100)
        print(invitelinknew)
        await ctx.send(invitelinknew)

    @commands.command()
    async def staff(self, ctx):
        """Affiche les membres du Staff"""
        await ctx.send("Pas encore disponible")

    @commands.command(aliases=['servs', 'serveur', 'serv'])
    async def serveurs(self, ctx):
        """Indique le nombre de serveurs sur lesquels le bot est actif."""
        try:
            #await ctx.send("Actuellement actif sur " + str(len(ctx.bot.guilds)) + " serveur(s).")
            print("Actuellement actif sur " + str(len(ctx.bot.guilds)) + " serveur(s).")
            x = ', '.join([str(server) for server in ctx.bot.guilds])
            y = len(ctx.bot.guilds)
            print("Server list: " + x)
            if y > 40:
                embed = discord.Embed(title="Actuellement actif sur " + str(y) + " serveurs:", description=config.err_mesg + "```json\nImpossible d'afficher plus de 40 serveurs !```", color=0xFFFFF)
                return await ctx.send(embed=embed)
            elif y < 40:
                embed = discord.Embed(title="Actuellement actif sur " + str(y) + " serveurs:", description="```json\n" + x + "```", color=0xFFFFF)
                return await ctx.send(embed=embed)
        except:
            await ctx.send(config.err_mesg)

    @commands.command(aliases=['servinfo', 'servi', 'si', 'serveuri'])
    async def serverinfo(self, ctx):
        """Affiche toutes les infos sur le serveur"""
        e = discord.Embed(title=f"Serveur : {ctx.guild}", description="Infos", color=0xeccd1c, timestamp=datetime.utcnow())
        e.set_thumbnail(url= ctx.guild.icon_url)
        e.add_field(name='Propriétaire', value= ctx.guild.owner)
        e.add_field(name='Region', value= ctx.guild.region)
        e.add_field(name='Securité', value= ctx.guild.verification_level)
        e.add_field(name='Invitation', value='En cours')
        e.add_field(name='Utilisateurs', value=len(ctx.guild.members))
        e.add_field(name='No', value='No')
        e.add_field(name='No', value='No')
        e.add_field(name='No', value='No')
        e.add_field(name='No', value='No')
        e.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
        await ctx.send(embed=e)

    @commands.command(aliases=['sa'])
    async def salons(self, ctx):
        """Affiche tous les salons/catégories avec leurs id"""
        await ctx.send("""Veuillez patienter, cette opération peut prendre un certain temps (en fonction du nombre de salons, et du temps de réponse de l'API Discord, *~affiché ci-dessous~*)""")
        latency = ctx.bot.latency  # Included in the Discord.py library
        # Send it to the user
        await ctx.send(f'`Temps de réponse : {latency}`')
        await ctx.send(""":warning: **Le Bot peut cesser de répondre pendant la récupération des salons**""")
        try:
            channels = ctx.guild.channels
            embed=discord.Embed(title=f"Salons et Catégories de {ctx.guild}", color=dec, timestamp=datetime.utcnow())
            embed.set_thumbnail(url = ctx.guild.icon_url)
            for channel in channels:
                embed.add_field(name=f"Salon/Catégorie : {channel.name}", value=f"  ID : {channel.id}", inline=True)
                embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=embed)
        except:
            ctx.send("Trop de Salons/Catégories.")

    @commands.command(aliases=['rol'], pass_context=True)
    async def roles(self, ctx):
        """Affiche tous les rôles avec leurs id"""
        await ctx.send("""Veuillez patienter, cette opération peut prendre un certain temps (en fonction du nombre de rôles, et du temps de réponse de l'API Discord, *~affiché ci-dessous~*)""")
        latency = ctx.bot.latency  # Included in the Discord.py library
        # Send it to the user
        await ctx.send(f'`Temps de réponse : {latency}`')
        await ctx.send(""":warning: **Le Bot peut cesser de répondre pendant la récupération des rôles**""")
        roles = ctx.guild.roles
        embed=discord.Embed(title="Roles", description=f"Serveur : {ctx.guild}", color=0xce0005, timestamp=datetime.utcnow())
        embed.set_thumbnail(url = ctx.guild.icon_url)
        for role in roles:
            embed.add_field(name=f"Role : {role.name}", value=f"ID : {role.id}", inline=False)
            embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
        await ctx.send(embed=embed)



    @commands.command(aliases=['ui', 'userinfo', 'u'])
    async def user(self, ctx, *, member: discord.Member = None):
        """Affiche toutes les infos sur quelqu'un"""
        if member is None:
            member = ctx.message.author
            roles = [role for role in member.roles]
            embed = discord.Embed(color = 0xF47B67, timestamp=datetime.utcnow())
            embed.set_thumbnail(url = member.avatar_url)
            embed.set_author(name=f"Infos sur {member.display_name}:", icon_url=member.avatar_url)
            embed.add_field(name="Pseudo sur ce serveur:", value=member.display_name, inline=True)
            embed.add_field(name="Nom d'utilisateur:", value=member, inline=True)
            embed.add_field(name="Statut", value=member.status, inline=True)
            embed.add_field(name="ID utilisateur:", value=member.id, inline=True)
            embed.add_field(name="Compte Bot:", value=member.bot, inline=True)
            embed.add_field(name="Création compte:", value=member.created_at, inline=True)
            embed.add_field(name="Role principal : ", value=member.top_role.mention, inline=True)
            embed.add_field(name=f"Roles : ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=True)
            embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=embed)
        else:
            roles = [role for role in member.roles]
            embed = discord.Embed(color = 0xF47B67, timestamp=datetime.utcnow())
            embed.set_thumbnail(url = member.avatar_url)
            embed.set_author(name=f"Infos sur {member.display_name}:", icon_url=member.avatar_url)
            embed.add_field(name="Pseudo:", value=member.display_name, inline=True)
            embed.add_field(name="Nom d'utilisateur:", value=member, inline=True)
            embed.add_field(name="Statut", value=member.status, inline=True)
            embed.add_field(name="ID utilisateur:", value=member.id, inline=True)
            embed.add_field(name="Bot:", value=member.bot, inline=True)
            embed.add_field(name="Création compte:", value=member.created_at, inline=True)
            embed.add_field(name="Role principal : ", value=member.top_role.mention, inline=True)
            embed.add_field(name=f"Roles : ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=True)
            embed.set_footer(text="Codé par Δnokino#7477", icon_url=(await self.bot.fetch_user('305066808660983811')).avatar_url)
            await ctx.send(embed=embed)

    @commands.command(name="avatar", aliases=['pp', 'av', 'userpp', 'upp'])
    async def _avatar(self, ctx, *, member: discord.Member = None):
        """Affiche la photo de profil de quelqu'un"""
        if member is None:
            member = ctx.message.author
            e = discord.Embed(description="Image de profil de {}".format(member.name), title='Avatar', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=member.avatar_url)
            e.set_footer(text="Codé par Δnokino#7477", icon_url=member.avatar_url)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(description="Image de profil de {}".format(member.name), title='Avatar', color=0xF47B67, timestamp=datetime.utcnow())
            e.set_image(url=member.avatar_url)
            e.set_footer(text="Codé par Δnokino#7477", icon_url=member.avatar_url)
            await ctx.send(embed=e)



def setup(bot):
    bot.add_cog(Info(bot))
