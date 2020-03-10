<h1 align=center> Discord.py Spotify embedding example code </h1>
<p align=center>Example code for discord.py spotify embeds</p>

<h2 align=center> Prerequisite </h2>
<p> You need both the discord.py and pendulum libary.</p>

<h3 align=center> Installing </h3>
<h4> Installing discord.py </h4>
<p1><a href="https://discordpy.readthedocs.io/en/latest/intro.html#installing">Discord.py </a></p1>
<p1> The official installation guide from Discord.py </p1>

<h4> Installing pendulum </h4>
<p1> <a href="https://pendulum.eustace.io/docs/">Pendulum </a> </p1>
<p1> The official installation guide from Pendulum. </p1>

<h4> Using PIP </h4>

```bash
pip install -U pendulum discord.py
```


<h2 align=center> Code preview </h2>

```py
import discord
from discord.ext import commands
from discord import Spotify
import pendulum

bot = commands.Bot(command_prefix="PREFIX HERE")

@bot.event 
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.command()
async def np(ctx, user: discord.Member=None):
    if user is None: #Checks if you tagged someone or wrote it yourself
        user=ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            embed=discord.Embed(title=activity.title, description=activity.artist, color=activity.color)
            embed.set_thumbnail(url=activity.album_cover_url)
            embed.add_field(name=activity.album, value=(f"Lengde: {pendulum.duration(seconds=activity.duration.total_seconds())}"), inline=True)
            embed.set_footer(text="Preben's Atago bot")
            await ctx.send (embed=embed)
            break #Without the break you will send both if and else
    else: #If you dont listen to spotify this will go off
        await ctx.send(f"{user.mention} Is not listening to music at the moment..")
        


bot.run('YOURTOKENHERE')
```
