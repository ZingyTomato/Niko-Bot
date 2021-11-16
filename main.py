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
import DiscordUtils

# Enable intents

intents = discord.Intents.default()
intents.members = True

# Define client prefix

client = commands.Bot(command_prefix = '.', intents=intents, help_command=None)
DiscordComponents(client)

# Define music for music command

music = DiscordUtils.Music()

# Set discord bot status

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))
    
# Global cooldowm and error handling

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Spammer detected!",description = f'Whoa whoa slow it down there buckaroo! You can execute this command in exactly {round(error.retry_after, 2)} seconds!',color = discord.Color.blue())
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.errors.CommandNotFound):
        embed=discord.Embed(title="Command not found! ",description = "My systems have detected that you have entered an invalid command!", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

        
# Leveling System

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json' , 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, random.randint(1,5))
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
    await client.process_commands(message)

# Update user data for leveling system

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0

async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        embed=discord.Embed(title="Level up!", description=f"{user.mention} has leveled up to level {lvl_end}!!", color = discord.Color.green())
        await message.channel.send(embed=embed)
        users[f"{user.id}"]['level'] = lvl_end

# Check level

@client.command()
@commands.cooldown(3, 15, commands.BucketType.user)
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
            lvl = users[str(id)]['level']
            embed=discord.Embed(title="Your current level", description=f"You are at level {lvl}!", color=discord.Colour.green())
            await ctx.reply(embed=embed)
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
            lvl = users[str(id)]['level']
            embed=discord.Embed(title="Your current level", description=f"{member} is now at level {lvl}!", color=discord.Colour.green())
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

# Slowmode command

@client.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(3, 15, commands.BucketType.user)
async def slowmode(ctx,time:int):
    try:
        if time == 0:
            embed= discord.Embed(title="Slowmode turned off!", description="Slowmode has been set to 0.", color=discord.Colour.blue())
            await ctx.channel.edit(slowmode_delay = 0)
            await ctx.reply(embed=embed)
        elif time > 21600:
            embed= discord.Embed(title="Slowmode limit passed!", description="You can't set the slowmode to be higher than 6 hours dumb dumb.", color=discord.Colour.blue())
            await ctx.reply(embed=embed)
            return
        else:
            await ctx.channel.edit(slowmode_delay = time)
            embed= discord.Embed(title="Slowmode changed!", description=f"Slowmode is now {time} seconds!", color=discord.Colour.green())
            await ctx.reply(embed=embed)
    except Exception:
        await print("Uh something went wrong.")


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
   embed.add_field(name = ".help", value = "Access a list of all commands.")
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
   embed.add_field(name = ".slowmode", value = "Change the slowmode to your desired value.")
   embed.add_field(name = ".level", value = "Check your level and flex on others.")
   embed.add_field(name = ".join", value = "Allow niko to join a VC.")
   embed.add_field(name = ".leave", value = "Allow niko to leave a VC.")
   embed.add_field(name = ".play", value = "Play a song of your choice using a youtube video's URL.")
   embed.add_field(name = ".pause", value = "Pause the song.")
   embed.add_field(name = ".resume", value = "Resume the song.")
   embed.add_field(name = ".queue", value = "View the queue for upcoming songs.")
   embed.add_field(name = ".loop", value = "Allow the song to play on loop. Same command to disable the loop.")
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
async def niko(ctx, *,msgAI):
    url = requests.get('http://api.brainshop.ai/get?bid=160296&key=APIKEY&uid=['+str(ctx.author.id)+']&msg='+msgAI)
    decode = json.loads(url.text)
    embed=discord.Embed(description = f"{decode['cnt']}")
    await ctx.reply(embed=embed)

# Wallpaper command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def wallpaper(ctx, *,wall):
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
  
# News command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def news(ctx, *,new):
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
        
# Weather command

@client.command()
@commands.cooldown(3, 4, commands.BucketType.user)
@commands.guild_only()
async def weather(ctx, *,weath):
    url = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+weath+'&appid=APIKEY')
    decode = json.loads(url.text)
    embed=discord.Embed(title=f"{decode['weather'][0]['main']}", description=f"{decode['weather'][0]['description']}")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)
 
# Lyrics command

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
@commands.guild_only()
async def lyrics(ctx, artist,*, title):
    url = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
    decode = json.loads(url.text)
    embed=discord.Embed(title=f"Lyrics for {title}", description=f"{decode['lyrics']}")
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

# Music commands

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def join(ctx):
    voicetrue = ctx.author.voice
    if voicetrue is None:
        embed=discord.Embed(title="Voice channel not found", description="You have not joined a voice channel!", color = discord.Color.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        return await ctx.reply(embed=embed)
    await ctx.author.voice.channel.connect()
    embed=discord.Embed(title="Joined voice channel", description="I am now in your voice channel!", color = discord.Color.green())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def leave(ctx):
    voicetrue = ctx.author.voice
    myvoicetrue = ctx.guild.me.voice
    if voicetrue is None:
        embed=discord.Embed(title="Voice channel not found", description="You have not joined a voice channel!", color = discord.Color.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        return await ctx.reply(embed=embed)
    if myvoicetrue is None:
        embed=discord.Embed(title="Voice channel not found", description="I am not currently in a voice channel!", color = discord.Color.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        return await ctx.reply(embed=embed)
    await ctx.voice_client.disconnect()
    embed=discord.Embed(title="Left voice channel", description="I have left your voice channel!", color = discord.Color.green())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        embed=discord.Embed(title="Song successfully found!", description=f"Now playing {song.name}!", color = discord.Color.green())
        await ctx.reply(embed=embed)
    else:
        song = await player.queue(url, search=True)
        embed=discord.Embed(title="Song successfully queued!", description=f"Queued {song.name}!", color = discord.Color.green())
        await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    embed=discord.Embed(title="Song paused!", description=f"Paused {song.name}!", color = discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    embed=discord.Embed(title="Song resumed!", description=f"Resuming {song.name}!", color = discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    embed=discord.Embed(title="Song stopped!", description=f"Stopped {song.name}!", color = discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        embed=discord.Embed(title="Loop enabled!", description=f"Enabled loop for {song.name}!", color = discord.Color.green())
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title="Loop disabled!", description=f"Disabled loop for {song.name}!", color = discord.Color.green())
        await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    embed=discord.Embed(title="Queue", description=f"**In queue :** {'  ,  '.join([song.name for song in player.current_queue()])}", color = discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    embed=discord.Embed(title="Now playing!", description=f"Currently playing {song.name}!", color = discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        embed=discord.Embed(title="Skipping song!", description=f"Skipped from {data[0]} to {data[1]}", color = discord.Color.green())
        await ctx.reply(embed=embed)
    else:
        embed=discord.Embed(title="Skipping song!", description=f"Skipped {data[0].name}", color = discord.Color.green())
        await ctx.reply(embed=embed)

@client.command()
@commands.cooldown(5, 30, commands.BucketType.user)
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    embed=discord.Embed(title="Removed song!", description=f"Removed {song.name} from queue", color = discord.Color.green())
    await ctx.reply(embed=embed)    

# More Error handling

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
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Member name not found!",description = "Please enter a members name! For example : **.ban Zingytomato#0604**", color=discord.Colour.red())
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
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Member name not found!",description = "Please enter a members name! For example : **.kick Zingytomato#0604**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@unban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Insufficient Permissions!",description = f"Don't be a doofus! You don't have the right permissions. Permissions needed {error.missing_perms}", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Member name not found!",description = "Please enter a members name! For example : **.unban Zingytomato#0604**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@slowmode.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Insufficient Permissions!",description = f"Don't be a doofus! You don't have the right permissions. Permissions needed {error.missing_perms}", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Duration not found!",description = "Please enter a specific time! For example : **.slowmode 69**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@wallpaper.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Wallpaper not found! ",description = "Please enter a wallpaper to search for! For example : **.wallpaper nature**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@news.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="News article not found! ",description = "Please enter a topic to search for! For example : **.news Discord**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@find.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Search query not found! ",description = "Please enter a search query! For example : **.find Discord**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)

@weather.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="City not found! ",description = "Please enter a city! For example : **.weather Bangalore**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
@niko.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Phrase not found! ",description = "Please enter a phrase to talk with Niko! For example : **.niko do you like School?**", color=discord.Colour.red())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.reply(embed=embed)
        
@play.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="URL not found! ",description = "Please enter a youtube URL to play!", color=discord.Colour.red())
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

# Calculator

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
