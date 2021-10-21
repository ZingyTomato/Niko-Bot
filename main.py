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
from googlesearch import search 
load_dotenv()
TOKEN = os.getenv('TOKEN')



client = discord.Client()
client2 = discord.Client()
client3 = discord.Client()





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
def get_quote_name():
    response = requests.get(
        "http://names.drycodes.com/1?nameOptions=boy_names"
    )
    json_data = json.loads(response.text)
    randname = json_data[0]
    return (randname)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Your Friendly Neighbourhood SpiderBot'))




@client2.event
async def on_ready(): 
    channel = client2.get_channel(767765551266398211) 
    await channel.send("I'm back online! Please wait for a few minutes while I get everything ready! If you are seeing this message repeatedly it means that my dumb owner, zingy :tomato: is constantly making changes.")
@client3.event
async def on_ready(): 
    channel = client3.get_channel(850251488339951627) 
    await channel.send("Why is nobody talking to me :( I'm sad :pepekms:")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hello_quotes = [
        'Get a life smh.',
        'Uhhhh hi?',
        'Who asked you?',
        'Are u a :monkey:?',
        'https://tenor.com/view/flushed-rickroll-flushed-rickroll-never-gonna-gif-20255515',
        'Didnt ask g.',
        'Okay who cares.',
        'More more!',
        'Ahahhahahaahah',
        'Welcome to hell :smiling_imp:.',
        
    ]
    
    if message.content == 'hai':
        response1 = random.choice(hello_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response1)
    if message.content == 'hello':
        response1 = random.choice(hello_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response1)
    if message.content == 'Hello':
        response1 = random.choice(hello_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response1)
    if message.content == 'Hai':
        response1 = random.choice(hello_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response1)

    if message.content == 'monk':
        await message.channel.send(':monkey: {} '.format(message.author.mention))
    if message.author == client.user:
        return
    if message.content == 'sus':
     response = "https://tenor.com/view/sus-fry-futurama-gif-4691459"
     await message.add_reaction("👍")
     await message.channel.send(response)
    if message.content == 'Sus':
     response = "https://tenor.com/view/sus-fry-futurama-gif-4691459"
     await message.add_reaction("👍")
     await message.channel.send(response)     
    if message.content == 'fudge':
        response11 = "https://tenor.com/view/stephen-colbert-fudge-yourself-gif-12825593"
        await message.add_reaction("👍")
        await message.channel.send(response11) 
    if message.content == ":KEKW:":
        response5 = "stop laughing. we only experience despair and depression -__-"
        await message.add_reaction("👍")
        await message.channel.send(response5) 
    if message.content == ":kekw:":
        response5 = "stop laughing. we only experience despair and depression -__-" 
        await message.add_reaction("👍")     
        await message.channel.send(response5)
    if message.content.startswith('im bored'):
        embedVar = discord.Embed(title="Epicc Joke")
        quote = get_quote()
        await message.add_reaction("👍")
        await message.channel.send(quote, embed=embedVar)
    if message.content.startswith('tell me a random name'):
        quote2 = get_quote_name()
        await message.add_reaction("👍")
        await message.channel.send(quote2)
    if message.content.startswith('im sad'):
        embed1 = discord.Embed(title="Inspirational Quote")
        quote1 = get_quote()
        await message.add_reaction("👍")
        await message.channel.send(quote1, embed=embed1)
    if message.content.startswith('meme'):
        def meme(ctx):
         client = commands.Bot(command_prefix="!")
        content = get("https://meme-api.herokuapp.com/gimme?Flags=nsfw=false").text
        data = json.loads(content,)
        meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
        await message.add_reaction("👍")
        await message.channel.send(embed=meme)
    if message.content == 'tom tom':
        response9 = "https://tenor.com/view/tom-go-tom-gif-20838220"
        await message.add_reaction("👍")
        await message.channel.send(response9)
    if message.content == 'ok':
        response17 = "https://tenor.com/view/kinblood-ko-boxing-knock-out-gif-12154201"
        await message.add_reaction("👍")
        await message.channel.send(response17) 
    if message.content == '.help':
        embed=discord.Embed(title="List of commands", description="""
Type .help to access this list again.
Type meme to view some of the cringiest memes that you have ever seen (totally not NSFW).
Type sus to well-
Type phys to make fun of people who like physics.
Type im sad to see some inspirational quotes.
Type im bored to cheer yourself up.
Type fudge to see steven colbert hold a cake.
Type hai to insult people who are being nice.
Type niko + blah blah to get a response from an AI (It's very cool).
Type gamble to take a gamble.
Type tell me a random name to as the name suggests-
Mention the creators name (if you know him/her/it) for some great insults.
Type !serverinfo to view info about the current server.
Type !kick + member to well... kick a member lol.
Type !wallpaper + blah blah to get a random wallpaper.
Type !news + topic to get the latest news.
Have any another ideas? DM the **OG** Anirudh.""")
        await message.add_reaction("👍")
        await message.channel.send(embed=embed)


        
    
    
     
    if message.author == client.user:
        return

    physcis_quotes = [
        'Lol nerd.',
        ':fire:',
        'Who cares about physics?',
        'f=ma.',
        'e=mc2. You are welcome :)',
        'My gosh you are such a nerd.',
        'Lol chemistry is better.',
        'Flames everywhere!',
        'Does it look lke i care?',
        'https://tenor.com/view/math-thinking-zach-galifianakis-formulas-numbers-gif-7715569',
        'p = m x v. Yeah I know super smart.',
        'I personally feel that...',
        'Great, the nerd is here!',
        'Go away!',
        
    ]

    if message.content == 'phys':
        response2 = random.choice(physcis_quotes)
        await message.channel.send(response2)
        await message.add_reaction("👍")
    if message.content == 'Phys':
        response2 = random.choice(physcis_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response2)    
    if message.content == 'Physics':
        response2 = random.choice(physcis_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response2)     
    if message.content == 'physics':
        response2 = random.choice(physcis_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response2) 
             
    if message.author == client.user:
        return

    xd_quotes_quotes = [
        "What is so funny? I do not get it!",
        'Hahaha funny.',
        'Totally the funniest thing ever!',
        'What is the date?',
        'Do you know a monkey?',
        'Boring.',
        '...',
        'Do u have a brain? It is not funny.',
        'Shake my head so predictable.',
        'You suck.',
        'Alright I am done with this.',
        'You have no sense of humour.',
        'Okay boomer.',
                
    ]

    if message.content == 'XD':
        response3 = random.choice(xd_quotes_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response3)
    if message.author == client.user:
        return

    lol_quotes = [
        "What is so funny? I don't get it!",
        'Hahaha funny.',
        'Totally the funniest thing ever!',
        'What is the date?',
        'Do you know a monkey?',
        'Boring.',
        '...',
        'Do you have a brain? It is not funny.',
        'Shake my head so predictable.',
        'You suck.',
        'Alright I am done with this.',
        'You have no sense of humour!',
        'Okay boomer.',
        'Wow you are so funny!',
        'That is so funny wow!',
        'Sorry but I just do not care.',
                
    ]

    if message.content == 'lol':
        lolresponse = random.choice(lol_quotes)
        await message.add_reaction("👍")
        await message.channel.send(lolresponse)
    if message.content == 'LOL':
        lolresponse = random.choice(lol_quotes)
        await message.add_reaction("👍")
        await message.channel.send(lolresponse)
    if message.content == 'LMAO':
        lolresponse = random.choice(lol_quotes)
        await message.add_reaction("👍")
        await message.channel.send(lolresponse)
    if message.content == 'lmao':
        lolresponse = random.choice(lol_quotes)
        await message.add_reaction("👍")
        await message.channel.send(lolresponse)
    if message.content == '69':
        await message.channel.send("Ha nice.")
        await message.add_reaction("👌")
    if message.content == '420':
        await message.channel.send("Ha nice.")
        await message.add_reaction("👌")
    if message.content == '69420':
        await message.add_reaction("👌")
        await message.channel.send("Ha nice.")
    if message.content == 'pog':
        await message.add_reaction("👌")
        await message.channel.send("Pogchamp.")

    if message.author == client.user:
        return

    name_quotes = [
        "Yeah what about him?",
        'He is my creator.',
        'He programmed me.',
        'Please do not bully.',
        'He is amazing!',
        'Lol he sucks.',
        '...',
        'Yea he is dumb.',
        'I do not have much to say about him.',
        'He is weird.',
        'I do not really ike him.',
        'Maybe he is your friend but he is not mine.',
        'He is a boomer.',
        'Ha.',
        'He is damn annoying shake my head.',
        'Sorry but I just do not care.',
                
    ]

    if message.content == 'ani':
        nameresponse = random.choice(name_quotes)
        await message.add_reaction("👍") 
        await message.channel.send(nameresponse)
               
    if message.content == 'Ani':
        nameresponse = random.choice(name_quotes)
        await message.add_reaction("👍")
        await message.channel.send(nameresponse)
        
    if message.content == 'zingy':
        nameresponse = random.choice(name_quotes)
        await message.channel.send(nameresponse)
        await message.add_reaction("👍")
    if message.content == 'Zingy':
        nameresponse = random.choice(name_quotes)
        await message.add_reaction("👍")
        await message.channel.send(nameresponse)
        
    if message.content == 'Anirudh':
        nameresponse = random.choice(name_quotes)
        await message.add_reaction("👍")
        await message.channel.send(nameresponse)
        
    if message.content == 'anirudh':
        nameresponse = random.choice(name_quotes)
        await message.add_reaction("👍")
        await message.channel.send(nameresponse)
    
    if message.content == 'xd':
        response3 = random.choice(xd_quotes_quotes)
        await message.add_reaction("👍")
        await message.channel.send(response3)
        
    if message.content == 'xD':
        response3 = random.choice(xd_quotes_quotes)
        await message.add_reaction("👍")  
        await message.channel.send(response3)   
    if message.content == 'XDD':
        response3 = random.choice(xd_quotes_quotes)
        await message.add_reaction("👍")  
        await message.channel.send(response3) 
        
    ping_quotes = [
        "DO U NOT HAVE ANYTHING ELSE TO DO? STOP PINGING",
        "GET OFF STOP BUGGING ME",
        'IM BUSY WHAT DO U WANT',
        'IM ON VACATION LEAVE ME ALONE',
        "https://tenor.com/view/rick-roll-gif-22683806",
        'GET A LIFE STOP PINGING',
        'GO STUDY OR SMTH LEAVE ME ALONE',
        'Do you have a brain? It is not funny.',
        '*deletes the server*',
        'What is your problem mate?',
        '..',
        'https://tenor.com/view/rickroll-rick-roll-gif-19877831',
        'https://tenor.com/view/challenge-find-out-when-this-gif-ends-rickroll-rickrolled-hidden-rickroll-gif-22493495',
        'https://tenor.com/view/itachi-meme-rick-roll-itachi-vs-sasuke-hidden-rick-roll-gif-21968202',
        'https://cdn.discordapp.com/attachments/852949806339063818/890091232808820736/saed.png',
        'https://tenor.com/view/rickroll-spongebob-gif-20016904',
        'https://tenor.com/view/rickroll-gif-22280972',
        'https://tenor.com/view/cute-cat-rick-roll-gif-22622972',
        'https://tenor.com/view/rickroll-yt-rewind-youtube-rewind-will-smith-prank-gif-21706791',
        'https://tenor.com/view/rickroll-rick-astley-pupzyy-never-gonna-give-you-up-meme-gif-20503685',
        'https://tenor.com/view/firefoxgaming-meme-rick-roll-rickrolled-kermit-gif-20211140',
        'https://tenor.com/view/among-us-spongebob-meme-patrick-hates-rick-roll-nopeuwu-gif-gif-20458465',
                
    ]
    
    if client.user.mentioned_in(message):
        response8 = random.choice(ping_quotes)
        await message.add_reaction("👍") 
        await message.channel.send(response8)
               
        
    gambling_quotes = [
        "Yes.",
        'No.',
        'Maybe.',
        'What is the date?',
        'I do not know.',
        'Search it on duckduckgo.',
        'Ask your mom.',
        'I am not telling.',
        'Ask tom tom.',
        'Follow the river and you will shiver!',
        'Ok ok ok.',
        'Why are you asking me?',
        "I don't care enough to give an answer.",
        "Don't bother me.",
        "Bugger of man.",
                
    ]
    
    if message.content == 'gamble':
      response3 = random.choice(gambling_quotes)
      await message.add_reaction("👍")
      await message.channel.send(response3)
      

CHANNEL_ID = 850247048636137509
@aiocron.crontab('0 8 * * *')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Yes, Thursday. Fun.")
    
    
    random_quotes = [
        "Haha.",
        'Ever wondered what the meaning of life is?',
        'What did u have for breakfast?',
        'Did you see the US Open?',
        'Whoever is ^ me will be banned *Hope it is not me which reveals how dead this chat is.*',
        'Boring.',
        '...',
        'To be honest what am I doing at this point.',
        'Did you know that-',
        "Is the week over yet? I can't take it anymore.",
        'Alright I am done with this.',
        'I am losing my mind stop-',
        'All systems operational!',
        'Boooooringgg.',
        'Is anybody here or am i just talking to myself?',
        'Can you bring food to the psat exam?',
        'I am hungry!',
   ]
CHANNEL_ID = 850251488339951627
@aiocron.crontab('0 */4 * * *')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    responserandom = random.choice([
        "Haha.",
        'Ever wondered what the meaning of life is?',
        'What did u have for breakfast',
        'Did you see the US Open?',
        'Whoever is ^ me will be banned!',
        'Boring.',
        '...',
        'To be honest what am I doing at this point?',
        'Did you know that-',
        "Is the week over yet? I can't take it anymore!",
        'Alright I am done with this!',
        'I am losing my mind stop-',
        'All systems operational!',
        'Find these messages annoying?',
        'Anybody saw squid game or whatever its called?',
        'Guess what i get to annoy you more often now!',
        'Is anybody here or am I just talking to myself?',
        'Can you bring food to the psat exam?',
        'Hahah eot in just 2 months you are welcome.',
        
    
    ])
    await channel.send(responserandom)   

CHANNEL_ID2 = 850247048636137509
@aiocron.crontab('0 12 * * *')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID2)
    responserandom3 = random.choice([
        "Imagine being in real life school!",
        "I do not go to school if that was not already obvious.",
        "I live in a server on a computer."


    ])
    await channel.send(responserandom3)

     
    






bot2 = commands.Bot(command_prefix='!')
@bot2.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await ctx.guild.kick(user)
  await ctx.send(f"{user} has been kicked aw shucks!")

@bot2.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)
  



bot3 = commands.Bot(command_prefix='n')
@bot3.command()
@commands.guild_only()
async def iko(ctx, *,msgAI=None):
    msgAI = msgAI or 'Hi'
    url = requests.get('http://api.brainshop.ai/get?bid=APIKEY&key=KEY&uid=['+str(ctx.author.id)+']&msg='+msgAI)
    decode = json.loads(url.text)
    await ctx.send(decode['cnt'])
  
bot4 = commands.Bot(command_prefix='!')
@bot4.command()
@commands.guild_only()
async def wallpaper(ctx, *,wall=None):
    wall = wall or "Nature"
    url = requests.get('https://pixabay.com/api/?key=APIKEYq='+wall)
    decode = json.loads(url.text)
    await ctx.send(decode['hits'][random.randint(0,19)]['largeImageURL'])
  
bot5 = commands.Bot(command_prefix='!')
@bot5.command()
@commands.guild_only()
async def news(ctx, *,new=None):
    new = new or "Bitcoin"
    url2 = requests.get('https://newsapi.org/v2/everything?q='+new+'&apiKey=APIKEY')
    decode = json.loads(url2.text)
    await ctx.send("**AUTHOR: **" + decode['articles'][random.randint(0,19)]['author'])
    await ctx.send("**TITLE: **" + decode['articles'][random.randint(0,19)]['title'])
    await ctx.send("**DESCRIPTION: **" + decode['articles'][random.randint(0,19)]['description'])
    await ctx.send("**URL: **" + decode['articles'][random.randint(0,19)]['url'])

bot6 = commands.Bot(command_prefix='!')
@bot6.command()
@commands.guild_only()
async def advice(ctx):
    url = requests.get('https://api.adviceslip.com/advice')
    decode = json.loads(url.text)
    await ctx.send(decode['slip']['advice'])
    
bot8 = commands.Bot(command_prefix='.')
@bot8.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Scraping the internet... {author} ")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(f"Here you go! : {j}")



loop = asyncio.get_event_loop()
loop.create_task(bot2.start('TOKEN'))
loop.create_task(bot3.start('TOKEN'))
loop.create_task(bot4.start('TOKEN'))
loop.create_task(bot5.start('TOKEN'))
loop.create_task(bot6.start('TOKEN'))
loop.create_task(bot8.start('TOKEN'))
loop.create_task(client.start('TOKEN'))
loop.create_task(client2.start('TOKEN'))
loop.create_task(client3.start('TOKEN'))
print("Connected to discord!")
loop.run_forever()







