# Niko-Bot
Niko is an open source Discord bot. Designed to add a little spice, sarcasm and jokes to your server :)

# List of commands
**.Help**
<br>
Access a list of all commands.
<br>
<br>
**.meme**
<br>
Experience some epic memes.
<br>
<br>
**.niko**
<br>
Chat with Niko. Example usage - .niko + your query
<br>
<br>
**.info**
<br>
View some information about me.
<br>
<br>
**.serverinfo**
<br>
See the statistics of your server.
<br>
<br>
**.wallpaper**
<br>
See a wallpaper based on your search. Example usage - .wallpaper + your query
<br>
<br>
**.ping**
<br>
Usually used for maintenance purposes.
<br>
<br>
**.kick**
<br>
Kick a member. Example usage - .kick + member
<br>
<br>
**.ban**
<br>
Ban a member. Example usage - .ban + member
<br>
<br>
**.unban**
<br>
Unban a member. Example usage - .unban + member
<br>
<br>
**.news**
<br>
See the latest news on your desired topic. Example usage - .news + your query
<br>
<br>
**.find**
<br>
Search the internet for quick facts/information.
<br>
<br>
**.advice**
<br>
Recieve advice from a robot.
<br>
<br>
**.weather**
<br>
See the weather from any city. Example usage - .weather + your city
<br>
<br>
**.calc**
<br>
Use a calculator to calculate things like 65 + 4
<br>
<br>
**.slowmode**
<br>
Set the slowmode to your desired limit. Example usage - .slowmode 69
<br>
<br>
**.level**
<br>
See what level you are on.
<br>

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

`pip3 install discord.py DiscordUtils[voice] discord_components google requests`
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
