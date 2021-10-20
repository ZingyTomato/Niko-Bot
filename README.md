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

`pip3 install -r requirements.txt`
<br>
<h2> Discord Token </h2>

Get your discord bot token and replace 'TOKEN' at the end of the file : 

loop.create_task(bot2.start('TOKEN'))
<br>
loop.create_task(bot3.start('TOKEN'))
<br>
loop.create_task(bot4.start('TOKEN'))
<br>
loop.create_task(bot5.start('TOKEN'))
<br>
loop.create_task(client.start('TOKEN'))
<br>
loop.create_task(client2.start('TOKEN'))
<br>
loop.create_task(client3.start('TOKEN'))

<br>
<h2> Get the API keys </h2>

Visit : `https://brainshop.ai/`, register a new brain and replace the API key with APIKEY in line 521 : 
<br>
`url = requests.get('http://api.brainshop.ai/get?bid=APIKEY&key=KEY&uid=['+str(ctx.author.id)+']&msg='+msgAI)`
<br>
<br>
Visit : `https://pixabay.com`, register an account and replace the API key with APIKEY in line 530 : 
<br>
`url = requests.get('https://pixabay.com/api/?key=APIKEYq='+wall)`
<br>
<br>
Visit : `https://newsapi.org/`, register an account and replace the API key with APIKEY in line 539:
<br>
`url2 = requests.get('https://newsapi.org/v2/everything?q='+new+'&apiKey=APIKEY')`

<h2> Bring the bot up </h2>
python3 main.py
