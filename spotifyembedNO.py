import discord
from discord.ext import commands
from discord import Spotify
import pendulum

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.command()
async def np(ctx, user: discord.Member=None):
    if user is None:
        user=ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            embed=discord.Embed(title=activity.title, description=activity.artist, color=activity.color)
            embed.set_thumbnail(url=activity.album_cover_url)
            embed.add_field(name=activity.album, value=(f"Lengde: {pendulum.duration(seconds=activity.duration.total_seconds()).in_words(locale='nb')}"), inline=True)
            embed.set_footer(text="Preben sin Atago bot")
            await ctx.send (embed=embed)
            break
    else:
        await ctx.send(f"{user.mention} hører ikke på musikk for øyeblikket.")

bot.run('YOURTOKENHERE')