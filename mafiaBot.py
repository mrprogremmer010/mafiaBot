import discord
from discord.ext import commands
import random
import os

from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("bot is online")

players_id = []
players = []
@client.command()
async def join(ctx):
    choice = ["murder","innocent","detective"]
    channel = ctx.channel
    author = ctx.author.mention
    if author in players:
        await ctx.send(f"{author} you are on the game please wait for more {10 - len(players)} players ")
    else:
        players_id.append(author.id)
        players.append(author)
        await channel.send(f"{author} you are on the game please wait for more {10-len(players)} players")
        await channel.send(f"now there is {players}")

    if len(players) == 1:
        for user_id in players:
            member = client.fetch_user(int(user_id))
            await member.send(random.choice(choice))
        @client.command()
        async def kill(ctx, *, words):
            await ctx.message.delete()
            await ctx.send(f"{words}")







client.run(os.getenv('BOT_TOKEN'))
