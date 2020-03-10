# Discord.py-Spotify-Embed
Example code for discord.py spotify embeds

## Prerequisite
discord.py and pendulum libary.


## Code preview
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
            break #Without the break you will send both if and elsew
    else: #If you dont listen to spotify this will go off
        await ctx.send(f"{user.mention} Is not listening to music at the moment..")
        


bot.run('YOURTOKENHERE')
```
