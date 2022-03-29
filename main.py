from discord.ext import commands
import discord

token = 'OTU4MDUxMzAxNzE4MTE0MzU0.YkHszg.CZQGbgNUrbXqj5ivSvtC8GVRW_Y'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def setupwelcome(ctx):
    global idwelcomechannel
    idwelcomechannel = ctx.channel.id
    channel = bot.get_channel(idwelcomechannel)
    await channel.send(f'Your welcome channel is setted up here! {ctx.author.mention}')

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
    channel = bot.get_channel(idwelcomechannel)
    await channel.send(embed=embed)

bot.run(token)