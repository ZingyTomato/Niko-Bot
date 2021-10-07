# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands, tasks
import requests
import json
from datetime import datetime
import threading
import asyncio
import aiohttp
from requests import get
import aiocron
from discord.ext.commands import Bot
load_dotenv()
TOKEN = os.getenv('TOKEN')



client = discord.Client()
def get_quote():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"
    )
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return (joke)
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Your Friendly Neighbourhood SpiderBot'))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hello_quotes = [
        'get a life smh',
        'uhhhh hi?',
        'who asked you?',
        'r u a :monkey:?',
        'https://tenor.com/view/flushed-rickroll-flushed-rickroll-never-gonna-gif-20255515',
        'didnt ask g',
        'ok who cares',
        'more more',
        'ahahhahahaahah',
        'welcome to hell',
        
    ]
    
    if message.content == 'hai':
        response1 = random.choice(hello_quotes)
        await message.channel.send(response1)
    if message.content == 'hello':
        response1 = random.choice(hello_quotes)
        await message.channel.send(response1)
    if message.content == 'Hello':
        response1 = random.choice(hello_quotes)
        await message.channel.send(response1)
    if message.content == 'Hai':
        response1 = random.choice(hello_quotes)
        await message.channel.send(response1)

    if message.content == 'monk':
        await message.channel.send(':monkey: {} '.format(message.author.mention))
    if message.author == client.user:
        return
    if message.content == 'sus':
     response = "https://tenor.com/view/sus-fry-futurama-gif-4691459"
     await message.channel.send(response)
    if message.content == 'Sus':
     response = "https://tenor.com/view/sus-fry-futurama-gif-4691459"
     await message.channel.send(response)     
    if message.content == 'fudge':
        response11 = "https://tenor.com/view/stephen-colbert-fudge-yourself-gif-12825593"
    if message.content == ":KEKW:":
        response5 = "stop laughing. we only experience despair and depression -__-"
    if message.content == ":kekw:":
        response5 = "stop laughing. we only experience despair and depression -__-"      
        await message.channel.send(response5)
    if message.content.startswith('im bored'):
        embedVar = discord.Embed(title="Epicc Joke")
        quote = get_quote()
        await message.channel.send(quote, embed=embedVar)
    if message.content.startswith('im sad'):
        embed1 = discord.Embed(title="Inspirational Quote")
        quote1 = get_quote()
        await message.channel.send(quote1, embed=embed1)
    if message.content.startswith('meme'):
        def meme(ctx):
         client = commands.Bot(command_prefix="!")
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content,)
        meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
        await message.channel.send(embed=meme)
    if message.content == 'tom tom':
        response9 = "https://tenor.com/view/tom-go-tom-gif-20838220"
        await message.channel.send(response9)
    if message.content == '.help':
        help = """`List of commands : 
.help to access this list again
meme to view some of the cringiest memes that you have ever seen (totally not NSFW)
sus to well-
phys to make fun of people who like physics
im sad to see some inspirational quotes
im bored to cheer yourself up
fudge to see steven colbert hold a cake
hai to insult people who are being nice
XD to `"""
        await message.channel.send(help)
    if message.content == "Niko":
        nik = "Niko here :sunglasses: Sup"
        await message.channel.send(nik)
    if message.content == "niko":
        nik = "Niko here :sunglasses: Sup"
        await message.channel.send(nik)
 
        
    
    
     
    if message.author == client.user:
        return

    physcis_quotes = [
        'lol nerd',
        ':fire:',
        'who cares about physcis',
        'f=ma',
        'e=mc2. ur welcome :)',
        'gosh ur such a nerd',
        'lol chem better',
        'flames everywhere',
        'does it look lke i care?',
        'https://tenor.com/view/math-thinking-zach-galifianakis-formulas-numbers-gif-7715569',
        'p = m x v yeah ik sooper smart',
        'i personally feel that...',
        'great the nerd is here',
        'go away',
        
    ]

    if message.content == 'phys':
        response2 = random.choice(physcis_quotes)
        await message.channel.send(response2)
    if message.content == 'Phys':
        response2 = random.choice(physcis_quotes)
        await message.channel.send(response2)    
    if message.content == 'Physics':
        response2 = random.choice(physcis_quotes)
        await message.channel.send(response2)     
    if message.content == 'physics':
        response2 = random.choice(physcis_quotes)
        await message.channel.send(response2)          
    if message.author == client.user:
        return

    xd_quotes_quotes = [
        "what's so funny? i dont get it",
        'hahaha funny',
        'totally the funniest thing ever',
        'whats the date?',
        'do you know a monkey?',
        'boring',
        '...',
        'do u have a brain? its not funny',
        'smh so predictable',
        'u suck',
        'alr im done with this',
        'u have no sense of humour',
        'ok boomer',
                
    ]

    if message.content == 'XD':
        response3 = random.choice(xd_quotes_quotes)
        await message.channel.send(response3)
    if message.content == 'xd':
        response3 = random.choice(xd_quotes_quotes)
        await message.channel.send(response3)
    if message.content == 'xD':
        response3 = random.choice(xd_quotes_quotes)
        await message.channel.send(response3)   
    if message.content == 'XDD':
        response3 = random.choice(xd_quotes_quotes)
        await message.channel.send(response3)           
    ping_quotes = [
        "DO U NOT HAVE ANYTHING ELSE TO DO? STOP PINGING",
        "GET OFF STOP BUGGING ME",
        'IM BUSY WHAT DO U WANT',
        'IM ON VACATION LEAVE ME ALONE',
        "https://tenor.com/view/rick-roll-gif-22683806",
        'GET A LIFE STOP PINGING',
        'GO STUDY OR SMTH LEAVE ME ALONE',
        'do u have a brain? its not funny',
        '*deletes the server*',
        'Whats ur problem mate',
        '..',
        'https://tenor.com/view/rickroll-rick-roll-gif-19877831',
        'https://tenor.com/view/challenge-find-out-when-this-gif-ends-rickroll-rickrolled-hidden-rickroll-gif-22493495',
        'https://tenor.com/view/itachi-meme-rick-roll-itachi-vs-sasuke-hidden-rick-roll-gif-21968202',
        'https://cdn.discordapp.com/attachments/852949806339063818/890091232808820736/saed.png',
                
    ]
    
    if client.user.mentioned_in(message):
        response8 = random.choice(ping_quotes)
        await message.channel.send(response8)
        
        
CHANNEL_ID = 850247048636137509
@aiocron.crontab('0 8 * * *')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Good morning! Last day of school! finally over jesus")



bot2 = commands.Bot(command_prefix='!')
@bot2.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await ctx.guild.kick(user)
  await ctx.send(f"{user} has been kicked sucessfully")

loop = asyncio.get_event_loop()
loop.create_task(bot2.start('TOKEN'))
loop.create_task(client.start('TOKEN'))
loop.run_forever()






