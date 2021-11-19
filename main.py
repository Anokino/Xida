# coding: utf8


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
from collections import Counter

#from mcsrvstat import ServerStatus

# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    import config  # config.py is required to run; found in the same directory.
    from config import release, cogs, botversion, des, pref, bbtoken, key, startup_extensions, logfile, err_mesg, err_mesg_pi, err_mesg_permission, dec, answers, default_rich_presence, mention, heightballp, hug_img, kiss_img # setup.py is used to get the version number
####################################Logs##############################################


# This code logs all events including chat to discord.log. This file will be overwritten when the bot is restarted - rename the file if you want to keep it.

#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

##################################################################################

bot = commands.Bot(description=des, command_prefix=pref, status=discord.Status.dnd, activity=discord.Game(name="ߒnnexion à Discord..")) #indiquez la description et le préfixe de votre bot (laissez les apostrophes)
client = discord.Client()
db = TinyDB('data.json')
Users = Query()
bot.remove_command('help')
#client = ksoftapi.Client(api_key=(os.environ['APIKEY']))



#Status Messages
async def status():
    while True:
        #names = [f'{pref}help | Xina', default_rich_presence, f'sur {len(bot.guilds)} serveurs', f'avec {len(bot.users)} utilisateurs']
        names = ['❌🛑❌🛑❌🛑❌', "❌Grosse MAJ❌", '🛑❌🛑❌🛑❌🛑', "❌Bot inutilisable❌"]
        #names = [f'{pref}help | Xina', 'Mise à jour terminée', f'sur {len(bot.guilds)} serveurs', f'avec {len(bot.users)} utilisateurs']
        #names = [f'{pref}help | Xina', '#Eurovision', f'Joyeux Eurovision !', 'Eurovision 64 edtion !']
        for name in names:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=name))
            await asyncio.sleep(3)



#async def my_background_task():
    while True:
        print("Statut-task executed")
        #counter = 0
        #while not self.is_closed():
            #counter += 1
        channel = bot.get_channel(609350080448692234)
        await channel.purge(limit=1)
        await asyncio.sleep(0.5) # channel ID goes here
        ip='minecraft3027.omgserv.com:10102'
        # Ok, we are going to start here
        print("Executing command: {0}".format(f'statut {ip}'))
        #await ctx.send("Ok, Veuillez patienter :D")
        # Fetch status

        try:
            status = ServerStatus(ip)
        except Exception as e:
            await channel.send(":x: Désolé, mais le serveur minecraft est down :c")
            print("Failed to find server: {0}")#.format(e))
            return

        # And the best part - send response!
        # Try sending image first
        try:
            await channel.send(file=discord.File(status.generate_status_image()))
            return
        except Exception as err:
            print(err)
        # If sending images fails, send text message
        response = "Players online: {0} \\ {1}\nMOTD: {2}\nVersion: {3}"
        formatted_response = response.format(status.online_players, status.max_players, status.motd, status.version)

        #await ctx.send("Here we go!")
        print("Response:\n{0}".format(formatted_response))
        await channel.send(formatted_response)
        status.generate_status_image()

        #await channel.send(counter)
        await asyncio.sleep(60) # task runs every 60 seconds


# Print the starting text
print('---------------')
print('Xina')
print('---------------')
print('Lancement Bot...')
# Setup basic logging for the bot

#logging.basicConfig(level=logging.DEBUG)

@bot.event
async def on_connect():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="ߓïnnexion à Discord.."))
    await asyncio.sleep(1.5)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="ߒnnexion à Discord.."))
    print('------------------------')
    print('Bot connecté à Discord')
    print('------------------------')
    await asyncio.sleep(0.7)

@bot.event
async def on_ready():
    for cog in cogs:
        #try:
            print('Loading %s', cog)
            bot.load_extension(f'cogs.{cog}')
        #except Exception:
        #    print('Failed to load %s', cog)
    f = open('banner.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    print('---------------------------')
    print("Bot en ligne!")
    print('---------------------------')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="ߔ䄃魡rrage.."))
    f = open('logo.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    print('---------------------------')
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("En cours d'exécution sur:", platform.system(), platform.release(), "(" + os.name + ")")
    print("Xina version:", botversion)
    print("Nom : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(f"Actuellement actif sur: {str(len(bot.guilds))} servers.")
    print('---------------------------')
    print("")
    print('---------------------------')
    print("Le Bot est démarré et prêt!")
    print('---------------------------')
    await asyncio.sleep(15)
    game = discord.Game(name=f"{pref}help | {len(bot.guilds)} serveurs !")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=game))
    await asyncio.sleep(5)
    bot.loop.create_task(status())
    #bot.loop.create_task(my_background_task())

    #logger.info("Bot started successfully.")


###################------------####################Autres######################--------------#########################



###################------------####################Events######################--------------#########################

@bot.event
async def on_guild_join(guild):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Nouveau serveur !"))
    await asyncio.sleep(8)
    game = discord.Game(name="{pref}help | Nous sommes maintenant dans {} serveurs!".format(len(list(bot.guilds))))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=game))
    await asyncio.sleep(20)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=default_rich_presence))
    print("J'ai rejoint un serveur ! Nous sommes maintenant dans {} serveurs.".format(len(list(bot.guilds))))
    # Send a message in the server's general chat after joining.
    general = find(lambda x: x.name == "generale", guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(f"Bonjour {guild} !")
    else:
        general2 = find(lambda x: x.name == "général", guild.text_channels)
        if general2 and general2.permissions_for(guild.me).send_messages:
            await general2.send(f"Bonjour {guild} !")
        else:
            general3 = find(lambda x: x.name == "general", guild.text_channels)
            if general3 and general3.permissions_for(guild.me).send_messages:
                await general3.send(f"Bonjour {guild} !")

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "bot": # We check to make sure we are sending the message in the general channel
            ctx = channel
            await ctx.send(f""" :inbox_tray: Bienvenue sur {ctx.guild} **{member}** !""")
            print(f"{datetime.utcnow()}| {member} a rejoins {ctx.guild}")
        if str(channel) == "bienvenue": # We check to make sure we are sending the message in the general channel
            ctx = channel
            await ctx.send(f""" :inbox_tray: Bienvenue sur {ctx.guild} **{member}** ! *Et bon jeu* :wink:""")
            print(f"{datetime.utcnow()}| {member} a rejoins {ctx.guild}")
    #await member.add_roles(479676712792358923, reason='Autorole')

@bot.event
async def on_member_remove(member): #Fonction quand quelqu'un quitte un serveur
    for channel in member.guild.channels:
        if str(channel) == "bot": # We check to make sure we are sending the message in the general channel
            ctx = channel
            await ctx.send(f""" :outbox_tray: {member} a quitté {ctx.guild}.""")
            print(f"{datetime.utcnow()}| {member} a quitté {ctx.guild}")
        if str(channel) == "bienvenue": # We check to make sure we are sending the message in the general channel
            ctx = channel
            await ctx.send(f""" :outbox_tray: {member} a quitté {ctx.guild}.""")
            print(f"{datetime.utcnow()}| {member} a quitté {ctx.guild}")


@bot.event
async def on_message(message):
    #try:
        if message.author == bot.user:
            return

        if message.author == 415595129328369675:
            return


        if message.content == ('<@552566569729916958>'):
            print(f"{datetime.utcnow()} | Bot mentionné")
            await message.channel.send(random.choice(config.mention))
            return


        user = message.author.name
        msg = message.content
        print(f"{datetime.utcnow()} | Discord tchat: {user}: {msg}")

        await bot.process_commands(message)
    #except:
        #print("Message envoyé impossible à encoder.")

@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return


    user = message.author.name
    msg = message.content
    print(f"{datetime.utcnow()} | Discord tchat: {user} a suppr: {msg}")

    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return


    user = before.author.name
    msg = before.content
    msg2 = after.content
    print(f"{datetime.utcnow()} | Discord tchat: {user} a modif: {msg} en {msg2}")

    await bot.process_commands(after)

@bot.event
async def on_command_error(ctx: commands.Context, error: Exception):
    """The event triggered when an error is raised while invoking a command.
    ctx   : Context
    error : Exception"""

    if hasattr(ctx.command, 'on_error'):
        return

    ignored = ()
    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
        return

    elif isinstance(error, commands.DisabledCommand):
        await ctx.send('{} has been disabled.'.format(ctx.command))
        return

    elif isinstance(error, commands.NoPrivateMessage):
        try:
            await ctx.send('{} can not be used in Private Messages.'.format(ctx.command))
            return
        except discord.Forbidden:
            pass

    elif isinstance(error, commands.BadArgument) or isinstance(error, commands.UserInputError):
            parent = ctx.command.full_parent_name
            if len(ctx.command.aliases) > 0:
                aliases = ' | '.join(ctx.command.aliases)
                fmt = '[%s | %s]' % (ctx.command.name, aliases)
                if parent:
                    fmt = parent + ' ' + fmt
                alias = fmt
            else:
                alias = ctx.command.name if not parent else parent + ' ' + ctx.command.name

            e = discord.Embed(colour=dec)
            e.add_field(name='Usage : -%s %s' % (ctx.command.name, ctx.command.signature if ctx.command.signature is not None else "No description"), value=" - " + (ctx.command.help if ctx.command.help is not None else "No description") + "\n - Alias : " + alias)
            await ctx.message.add_reaction(emoji="❗")
            return await ctx.send(embed=e)
    #User input error
    #elif isinstance(error, commands.UserInputError):
        #pages = await bot.formatter.format_help_for(ctx, ctx.command)
        #for page in pages:
            #helpText = page.split('\n') #get each line
            #usageMessage = helpText[1:-1] #remove ``` at begining and end who make the block

            #em = discord.Embed(title = "Usage : " + usageMessage[0], description = '\n'.join(usageMessage[1:]),
                       #colour = discord.Colour.blue()
                       #)
            #await ctx.send(embed=em)
            #await ctx.message.add_reaction(emoji="❗")
        #return

    #Command Not Found
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction(emoji="❌")
        print(f'Commande inexistante écrite par {ctx.author.name}')
        msg = ctx.message.content
        await ctx.send(f" ``{msg}`` : Commande Inexistante")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await asyncio.sleep(0.5)
        await ctx.channel.purge(limit=1)
        return

    #Missing author required permission
    elif isinstance(error, commands.MissingPermissions):
        await ctx.message.add_reaction(emoji="⚠")
        await ctx.send("Permissions manquantes")
        return

    #print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    #traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)








###############-------------###################Commandes#######################-------------#############################

#@bot.command(name="help", aliases=['h'])
#async def _help(self, ctx, command_name=None):
#   """Affiche ce message"""
#
#    if command_name is not None:
#        await ctx.invoke(self.bot.get_command("usage"), command_name)
#    else:
#        em = discord.Embed(colour=discord.Colour.blue())
#        em.set_author(name="Aide de " + self.bot.user.name + ":", icon_url=self.bot.user.avatar_url)
#        em.set_footer(text="test",
#                        icon_url=(await self.bot.fetch_user('398486141843800074')).avatar_url)
#        for cog in self.bot.cogs:
#            help_message = ""
#            for commnd in self.bot.get_cog(cog).get_commands():
#                help_message += "\n - " + commnd.name + " : " + str(commnd.help)
#            if help_message is "":
#                continue
#            else:
#                em.add_field(name=cog.replace('_', ' '), value=help_message + "\n", inline=False)
#        await ctx.send(embed=em)

#@bot.command()
#async def help(ctx):
    #await ctx.send_help()
    #page = await ctx.send_help()
    #for page in pages:
        #helpText = page.split('\n') #get each line
        #usageMessage = helpText[1:-1] #remove ``` at begining and end who make the block
        #await ctx.send_help()
        #e = discord.Embed(description="Aide Xina", title='*En cours*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
        #e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png")
        #e.add_field(name='`Test`', value=page) #titre de la case, sous-titre
        #e.add_field(name='`Divers`', value='Toutes les commandes utiles')
        #e.add_field(name='`Modération`', value='Commandes de modération')
        #e.add_field(name='`Fun`', value='Les commandes pour s\'amuser !')
        #e.set_footer(text='Bot en dévellopement') #sous-titre de l'embed
        #if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
                #e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
        #await ctx.send(embed=e) #envoyer l'embed
    #e = discord.Embed(description="Aide Xinatitle='*Catégories*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    #e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embed
    #e.add_field(name='`Info`', value='Infos diverses') #titre de la case, sous-titre
    #e.add_field(name='`Divers`', value='Toutes les commandes utiles')
    #e.add_field(name='`Modération`', value='Commandes de modération')
    #e.add_field(name='`Fun`', value='Les commandes pour s\'amuser !')
    #e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    #if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            #e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    #await ctx.send(embed=e) #envoyer l'embed

#@bot.command(aliases=['Info', 'Infos', 'INFO', 'INFOS']) #tous les "alias" souhaités pour la commande
#async def help_info(ctx):
#    e = discord.Embed(description="Aide Xina™", title='*Infos*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
#    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embed
#    e.add_field(name='`botinfo`', value='Infos sur le bot') #titre de la case, sous-titre
#    e.add_field(name='`serverinfo`', value='Infos sur le serveur')
#    e.add_field(name='`invite`', value='Inviter le bot sur votre serveur')
#    e.add_field(name='`commande`', value='Non plus !')
#    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
#    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
#            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
#    await ctx.send(embed=e) #envoyer l'embed

#@bot.command(aliases=['help diver', 'help divers', 'aide divers', 'HELP DIVERS'])
#async def help_divers(ctx):
#    e = discord.Embed(description="Aide Xina™", title='*Divers*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
#    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embed
#    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
#    e.add_field(name='`2`', value='2. 1')
#    e.add_field(name='`3`', value='3. 1')
#    e.add_field(name='`4`', value='4. 1')
#    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
#    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
#            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
#    await ctx.send(embed=e) #envoyer

#@bot.command()
#async def help_moderation(ctx):
#    e = discord.Embed(description="Aide Xina™", title='*Modération*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
#    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embed
#    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
#    e.add_field(name='`2`', value='2. 1')
#    e.add_field(name='`3`', value='3. 1')
#   e.add_field(name='`4`', value='4. 1')
#    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
#    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
#            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
#    await ctx.send(embed=e) #envoyer

#@bot.command()
#async def help_fun(ctx):
#    e = discord.Embed(description="Aide Xina™", title='*Fun*', color=(dec), timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
#    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embed
#    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
#    e.add_field(name='`2`', value='2. 1')
#    e.add_field(name='`3`', value='3. 1')
#    e.add_field(name='`4`', value='4. 1')
#    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
#    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
#            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
#    await ctx.send(embed=e) #envoyer

#@bot.command()
#async def help_admin(ctx):
#    e = discord.Embed(description="Aide Xina™", title='*Administrateur*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
#    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/557926779768274975/logo.png") #icone de l'embe
#    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
#            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
#            e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails')
#    await ctx.send(embed=e) #envoyer




#@bot.command(aliases=['', 'hel', 'he', 'bruh'])
#async def he(ctx):
    #await ctx.send('Commande inexistante, ``{pref}help`` pour l\'aide.')

@bot.command(aliases=['request'])
async def register(ctx, botname, botid):
	apdev = bot.get_guild(501064268737937408)
	rq = apdev.get_channel(504829648996270080)
	e = discord.Embed(description='Bot request', title=f'{botname}', color=1565439, timestamp=datetime.utcnow())
	e.add_field(name=f'ID : {botid}', value=f'Requested by {ctx.author} at {datetime.utcnow()}')
	e.add_field(name=f'Invite link', value=f'https://discordapp.com/oauth2/authorize?client_id={botid}&scope=bot&permissions=0')
	e.set_footer(text='type k!request <bot name> <bot id> to request yours.')
	await rq.send(embed=e)
	await ctx.send(f"Votre bot, {botname}, à été proposé avec succès et devrait bientôt être ajouté. Vous pouvez suivre l'avancement de votre demande dans <#504829648996270080>.")

@commands.command(aliases = ["mcsuggestion"])
async def mcsug(self, ctx, *, suggestion):
    """Pour faire une suggestion par rapport au serveur minecraft"""
    await ctx.message.delete()
    asyncio.sleep(0.2)
    e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
    e.set_thumbnail(url="http://pcomstudentcouncil.com/wp-content/uploads/2018/05/suggestion-box-e1527787946907.jpg")
    e.add_field(name=f'Demandé par {ctx.author.name} ', value=suggestion)
    e.set_footer(text=f'Réagissez avec les réactions ci-dessous pour donner votre avis !')
    m = await ctx.send(embed=e)
    asyncio.sleep(0.3)
    await m.add_reaction(emoji="✅")
    asyncio.sleep(0.2)
    await m.add_reaction(emoji="❌")

@commands.command(aliases = ["bugreport"])
async def bug(self, ctx, *, bug):
    """Pour signaler un bug sur le serveur minecraft"""
    await ctx.message.delete()
    asyncio.sleep(0.2)
    e = discord.Embed(color=(dec), timestamp=datetime.utcnow())
    e.set_thumbnail(url="http://pcomstudentcouncil.com/wp-content/uploads/2018/05/suggestion-box-e1527787946907.jpg")
    e.add_field(name=f'Signalé par {ctx.author.name} ', value=bug)
    e.set_footer(text=f'Réagissez avec les réactions ci-dessous si vous êtes d\'accord avec ce signalement')
    m = await ctx.send(embed=e)
    asyncio.sleep(0.8)
    await m.add_reaction(emoji="✅")
    asyncio.sleep(0.8)
    await m.add_reaction(emoji="❌")

@bot.command()
async def autodestruct(ctx):
    await ctx.send('3')
    await ctx.send('2')
    await ctx.send('1')
    await ctx.send('Autodestruction')


@bot.command()
async def code75478efr(ctx):
    rnd = randint(0, 9999999999999999)
    await ctx.send(rnd)



@bot.command()
async def commande314358425(ctx):
    await ctx.send("Non cette commande ne sert à rien")
    await asyncio.sleep(8)
    await ctx.send("J'ai dis que ca ne sert à rien, pourquoi vous attendez quelque chose ?")
    await asyncio.sleep(8)
    await ctx.send("Enfin...")
    await asyncio.sleep(3)
    await ctx.send("Non je n'ai pas le droit de dire quoi que ce soit")
    await asyncio.sleep(10)
    await ctx.send("Je dois avouer que c'est tentant.")
    await asyncio.sleep(2)
    await ctx.send("Mais non je résiste")
    await asyncio.sleep(8)
    await ctx.send("Rooh je ne sais pas si je le dis je penses qu'il va m'en vouloir")
    await asyncio.sleep(2)
    await ctx.send("Vous pensez que je devrais le dire ?")
    await asyncio.sleep(8)
    await ctx.send("Mouais.")
    await asyncio.sleep(5)
    await ctx.send("Bon allez, tant pis")
    await asyncio.sleep(2)
    await ctx.send("Attention je vais le dire dans :")
    await asyncio.sleep(1)
    await ctx.send("3")
    await asyncio.sleep(1)
    await ctx.send("2")
    await asyncio.sleep(1)
    await ctx.send("1")
    await asyncio.sleep(2)
    await ctx.send("Joyeux poisson d'avril !")

#@bot.command()
#async def dynmap(ctx):
#    embed = discord.Embed(color = 0xF47B67)
#    embed.set_thumbnail(url="https://i.imgur.com/nvIvqtm.png")
#    embed.add_field(name="Dynmap", value="http://ayc.craft.gg:40008")
#    await ctx.send(embed=embed)


    #print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.guild.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

@bot.command()
async def avatar268(ctx, *, member: discord.Member = None):
    embed = discord.Embed(color = 0xF47B67)
    embed.add_field(name="Avatar de:", value=member)
    embed.add_field(name="Image :", value=member.avatar_url)
    await ctx.send(embed=embed)






@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick445972(ctx, member: discord.Member):
        if ctx.message.author.server_permissions.kick_members:
            #await bot.delete_message(ctx.message)
            #await bot.kick(member)
            await ctx.send(member + " a été kick")
        else:
            await ctx.send("Tu n'as pas la permission de kick les membres.")

@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True)
async def insult(ctx):
    """Says something mean about you."""
    await ctx.send(ctx.message.author.mention + " " + random.choice(config.answers))  # Mention the user and say the insult


#@bot.command()
#async def ball8(ctx, *, question):
    #e = discord.Embed(title=f'8 Ball', color=(dec), timestamp=datetime.utcnow())
    #e.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Magic_eight_ball.png")
    #e.add_field(name=f'Question : {question}', value =f'Ma réponse: {random.choice(config.heightballp)}')
    #e.set_footer(text=f'Demandé par {ctx.author.name}')
    #await ctx.send(embed=e)

@bot.command(pass_context=True)
async def blabla(ctx):
    url = await ctx.send("Webhook URL: ")
    embed = {}
    embedtitle = input("Embed title: ")
    embed["title"] = embedtitle
    embeddesc = input("Embed description: ")
    embed["description"] = embeddesc
    while True: #Thumbnail (optional)
        thumbnailornot = input("Add a thumbnail? (Yes/no): ")
        if thumbnailornot.lower() == 'yes':
            embedthumbnailurl = input("Enter a thumbnail URL: ")
            embed['thumbnail'] = {"url": embedthumbnailurl}
            break
        elif thumbnailornot.lower() == 'no':
            break
        else:
            print("Please enter either 'yes' or 'no' (without quotes).")
    embedfieldnum = input("How many fields in the embed? (Enter a number, 0 for none): ")
    try: embedfieldnum = int(embedfieldnum)
    except: print("You were supposed to enter a number - we'll assume you meant 0.")
    if embedfieldnum is not 0:
        embed['fields'] = []
        for fieldnum in range(embedfieldnum):
            fieldtitle = input("Field {} Title: ".format(fieldnum+1))
            fieldtext = input("Field {} Content: ".format(fieldnum+1))
            embed['fields'].append({"name":fieldtitle,"value":fieldtext})
    embedcolor = input("Embed Hex Color (6 Digit Hex): ")
    embedcolor = int(embedcolor, 16)
    embed["color"] = embedcolor
    print(embed)
    data = {"embeds": [embed]}
    requests.post(url,json=data)



#@bot.command()
#async def g_search(ctx, *, image):

    #await ctx.send(embed=e)


# It's reccommended that you keep the logout command disabled, especially running on multiple servers.

# @bot.command(pass_context = True)
# async def logout(ctx):
##    """Disconnects the bot from all servers."""
# if ctx.message.author.server_permissions.administrator:
# await ctx.send("**Goodbye!** :zzz:")
##        print("Exiting bot...")
# await bot.logout()
# else:
# await bot.say(config.err_mesg_permission)

##############################Partie Musique#####################################################

#Dans le cogs

##############################Lancement############################################################
# Read bot token from "config.py" (which should be in the same directory as this file)

#bot.run(bot.run(os.environ['TOKEN']))
bot.run('NjMyNjMzMzY5ODYzMzg5MjA3.XaIPyA.fc00tJJngRgbr-HmeuTuv0S7bfk')
#Lancer le bot. Remplacez token par votre token et laissez les apostrophes

