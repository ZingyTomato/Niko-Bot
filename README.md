# Niko-Bot
A work in progress discord bot. Does everything from memes to a chatbot.

Invite Link : `https://discord.com/api/oauth2/authorize?client_id=890816070322098197&permissions=534991339334&scope=bot`

# Requirements
`python3`
<br>
`python3-pip`

# Installation
<h2>Clone the repository</h2>
git clone https://github.com/ZingyTomato/Niko-Bot.git && cd Niko-Bot
<br>
<h2>Install Required Packages</h2>

`pip3 install pycord requests aiohttp datetime discord_components json google`
<br>
<h2> Discord Token </h2>

Get your discord bot token and replace 'TOKEN' at the end of the file : 

client.run("TOKEN")

<br>
<h2> Get the API keys </h2>

Visit : `https://brainshop.ai/`, register a new brain and replace the API key with APIKEY:
<br>
`url = requests.get('http://api.brainshop.ai/get?bid=APIKEY&key=KEY&uid=['+str(ctx.author.id)+']&msg='+msgAI)`
<br>
<br>
Visit : `https://pixabay.com`, register an account and replace the API key with APIKEY: 
<br>
`url = requests.get('https://pixabay.com/api/?key=APIKEYq='+wall)`
<br>
<br>
Visit : `https://newsapi.org/`, register an account and replace the API key with APIKEY:
<br>
`url2 = requests.get('https://newsapi.org/v2/everything?q='+new+'&apiKey=APIKEY')`
<br>
<br>
Visit : `https://home.openweathermap.org/users/sign_up`, register an account and replace the API key with APIKEY:
<br>
`url = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+weath+'&appid=APIKEY')`
<br>

<h2> Bring the bot up </h2>
python3 main.py
