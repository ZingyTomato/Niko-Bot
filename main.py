# Import all required libraries

import discord
import os
import requests
import json
import random
from requests import get
from discord.ext import commands
import time
from googlesearch import search
import aiohttp
from discord_components import *
import datetime

# Enable intents

intents = discord.Intents.default()
intents.members = True

# Define client prefix

client = commands.Bot(command_prefix = '.', intents=intents)
DiscordComponents(client)

# Set discord bot status

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.Help'))
    
# Global cooldowm

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Spammer detected!",description = f'Whoa whoa slow it down there buckaroo! You can execute this command in exactly {round(error.retry_after, 2)} seconds!',color = discord.Color.blue())
        await ctx.reply(embed=embed)
        

# Logging

@client.event
async def on_message_delete(message):
    embed = discord.Embed(title=f"{message.author.name} has deleted a message! What is he hiding?", color=discord.Colour.red())
    embed.add_field(name = "Deleted Message", value = f"{message.content}", inline = False)
    channel = discord.utils.get(client.get_all_channels(), name="logs")
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
    embed= discord.Embed(title=f"{message_before.author.name} has edited a message! Caught you red handed.", color=discord.Colour.green())
    embed.add_field(name = "Message Before Edit", value = f"{message_before.content}", inline = False)
    embed.add_field(name = "Edited Message", value = f"{message_after.content}", inline = False)
    channel = discord.utils.get(client.get_all_channels(), name="logs")
    await channel.send(embed=embed)


# Info command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def info(ctx):
   embed=discord.Embed(title="Hey there! I'm Niko 2.0, the next generation Niko.",description="Here's a few questions about me answered.",color =   discord.Colour.red(), inline = False)
   embed.add_field(name = "Who am I?", value = """I am a more efficient and a complete rewrite (kind of) of the original Niko that you all know and "love".""", inline = False)
   embed.add_field(name = "What happened to the old Niko?", value = "Well... he's no longer here. He was a bloated mess.", inline = False)
   embed.add_field(name= "What if I want to request a feature?", value = "As always, if you have any feature requests, kindly dm the **OG** Anirudh :)", inline = False)
   embed.add_field(name = "Why were some responses removed?", value = "They were most likely useless.", inline = False)
   embed.add_field(name = "What can you do?", value = "To find out what I can do, simple type `.Help`", inline = False)
   embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
   await ctx.reply(embed=embed)

# Meme command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme?Flags=nsfw=false").text
    data = json.loads(content,)
    embed = discord.Embed(title=f"{data['title']}", color = discord.Color.random()).set_image(url=f"{data['url']}")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Help command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def Help(ctx):
   embed=discord.Embed(title="Help Center",description="Here's a list of all my commands.",color = discord.Colour.green())
   embed.add_field(name = ".Help", value = "Access a list of all commands.")
   embed.add_field(name = ".meme", value = "Experience some epic memes.")
   embed.add_field(name = ".niko", value = """Chat with Niko. Example usage - ** .niko + your query**""")
   embed.add_field(name = ".info", value = "View some information about me.")
   embed.add_field(name = ".serverinfo", value = "See the statistics of your server.")
   embed.add_field(name = ".wallpaper", value = "See a wallpaper based on your search. Example usage -  **.wallpaper + your query**")
   embed.add_field(name = ".ping", value = "Usually used for maintenance purposes.")
   embed.add_field(name = ".kick", value = "Kick a member. Example usage - **.kick + member**")
   embed.add_field(name = ".ban", value = "Ban a member. Example usage - **.ban + member**")
   embed.add_field(name = ".unban", value = "Unban a member. Example usage - **.unban + member**")
   embed.add_field(name = ".news", value = "See the latest news on your desired topic. Example usage -  **.news + your query**")
   embed.add_field(name = ".find", value = "Search the internet for quick facts/information.")
   embed.add_field(name = ".advice", value = "Recieve advice from a robot.")
   embed.add_field(name = ".weather", value = "See the weather from any city. Example usage -  **.weather + your city**")
   embed.add_field(name = ".calc", value = "Use a calculator to calculate things like **65 + 4**")
   embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
   await ctx.reply(embed=embed)
   await ctx.send(
        "**Important Links**",
        components = [
            [
                Button(style=5, label ="Visit Project!", custom_id = "button1", url="https://github.com/ZingyTomato/Niko-Bot"),
                Button(style=5, label ="Invite me!", custom_id = "button2", url="https://discord.com/oauth2/authorize?client_id=890816070322098197&permissions=534991339334&scope=bot")
            ]
        ]
    )

# Server information command

format = "%a, %d %b %Y | %H:%M:%S %ZIST"

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def serverinfo(ctx):
    embed = discord.Embed(
        color = discord.Color.purple()
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed=discord.Embed(title=f"Information About **{ctx.guild.name}**")
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name="Owner", value=f"{ctx.guild.owner}", inline = False)
    embed.add_field(name="Location", value=f"{ctx.guild.region}", inline = False)
    embed.add_field(name="Creation Date", value=f"{ctx.guild.created_at.strftime(format)}", inline = False)
    embed.add_field(name="Channels", value=f"**{channels}** Channels, **{text_channels}** Text, **{voice_channels}** Voice", inline = False)
    embed.add_field(name="Members", value=f"{ctx.guild.member_count}", inline = False)
    embed.add_field(name="Categories", value=f"{categories}", inline = False)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# AI chatbot command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def niko(ctx, *,msgAI=None):
    msgAI = msgAI or 'Hi'
    url = requests.get('http://api.brainshop.ai/get?bid=160296&key=APIKEY&uid=['+str(ctx.author.id)+']&msg='+msgAI)
    decode = json.loads(url.text)
    embed=discord.Embed(description = f"{decode['cnt']}")
    await ctx.reply(embed=embed)

# Wallpaper command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def wallpaper(ctx, *,wall=None):
    wall = wall or "Nature"
    url = requests.get('https://pixabay.com/api/?key=APIKEY&q='+wall)
    decode = json.loads(url.text)
    embed=discord.Embed(title=f"Results for {wall}",color=discord.Color.orange()).set_image(url=f"{decode['hits'][random.randint(0,19)]['largeImageURL']}")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Ping command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def ping(ctx):
        embed=discord.Embed(title="Ping results",color = discord.Colour.blue())
        embed.add_field(name = "Bot Latency (Under 500 is good)", value = f"{round(client.latency * 1000)}ms")
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

# Kick command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await ctx.guild.kick(user)
  embed=discord.Embed(title="Member kicked",description = f"{user} has been kicked!")
  embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
  await ctx.reply(embed=embed)

# Ban command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason="No reason provided!"):
    embed=discord.Embed(title="Member banned",description = f"{member.name} has been banned!", color=discord.Colour.red())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)
    await member.ban(reason=reason)

# Unban command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            embed=discord.Embed(title="Member unbanned",description = f"{member_name} has been unbanned!", color=discord.Colour.blue())
            await ctx.reply(embed=embed)
            return
    embed=discord.Embed(title="Member not found",description = f"{member} was not found!", color=discord.Colour.green())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Check if user has permissions

@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Insufficient Permissions!",description = f"Don't be a doofus! You don't have the right permissions. Permissions needed {error.missing_perms}", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MemberNotFound):
        embed=discord.Embed(title="Member not found!",description = "My systems have detected that you have entered an invalid member name.", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)



@kick.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Insufficient Permissions!",description = f"Don't be a doofus! You don't have the right permissions. Permissions needed {error.missing_perms}", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MemberNotFound):
        embed=discord.Embed(title="Member not found!",description = "My systems have detected that you have entered an invalid member name.", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@unban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Insufficient Permissions!",description = f"Don't be a doofus! You don't have the right permissions. Permissions needed {error.missing_perms}", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

# News command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def news(ctx, *,new=None):
    new = new or "Bitcoin"
    url2 = requests.get('https://newsapi.org/v2/everything?q='+new+'&apiKey=APIKEY')
    decode = json.loads(url2.text)
    embed=discord.Embed(title=f"{decode['articles'][random.randint(0,19)]['title']}",color=discord.Colour.teal())
    embed.add_field(name = "Author", value = f"{decode['articles'][random.randint(0,19)]['author']}", inline = False)
    embed.add_field(name = "Description", value = f"{decode['articles'][random.randint(0,19)]['description']}", inline = False)
    embed.add_field(name = "Url", value = f"{decode['articles'][random.randint(0,19)]['url']}", inline = False)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Search command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def find(ctx,*, query):
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        embed=discord.Embed(title="Results from the internet")
        embed.add_field(name = "Top result", value = f"{j}")
        embed.set_thumbnail(url = f"{j}")
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

# Advice command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def advice(ctx):
    url = requests.get('https://api.adviceslip.com/advice')
    decode = json.loads(url.text)
    embed=discord.Embed(title="Your advice", description=f"{decode['slip']['advice']}", color = discord.Color.purple())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Weather command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def weather(ctx, *,weath=None):
    weath = weath or "Bangalore"
    url = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+weath+'&appid=APIKEY')
    decode = json.loads(url.text)
    embed=discord.Embed(title=f"{decode['weather'][0]['main']}", description=f"{decode['weather'][0]['description']}")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Calcultor

# Define buttons

buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]

# Calculating answer

def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result

# Execute calculator

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
async def calc(ctx):
    m = await ctx.send(content='Loading Calculators...')
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s calculator  |  {ctx.author.id}', description=expression,
                        timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
            0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                                timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)

# See if the bot is up

print("I'm ready!")

# Run the bot. Replace 'TOKEN' with your bot token

client.run("TOKEN")
