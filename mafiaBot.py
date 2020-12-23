import discord
from discord.ext import commands
from discord.ext.tasks import loop
import random
import os


client = commands.Bot(command_prefix = "!")
intents = discord.Intents(messages=True, guilds=True).all()
intents.members = True

@loop(seconds=1)
async def chng_stat():
	await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name=f'mafia with {len(client.guilds)} servers'))


@client.event
async def on_ready():
    chng_stat.start()
    print("bot is online")


players_id = []
players = {}
@client.command()
async def join(ctx):
    choice = ["murder","innocent","detective"]
    channel = ctx.channel
    author = ctx.author.mention
    author_id = ctx.author.id
    if author in players:
        await ctx.send(f"{author} you are on the game please wait for more {10 - len(players)} players ")
    else:
        players_id.append(author_id)
        # players.append(author)
        pc_choice = random.choice(choice)
        players[author] = pc_choice
        choices = " ".join(players.keys())
        await mur()
        await dv()
        await channel.send(f"{author} you are on the game please wait for more {10-len(players)} players")
        await channel.send(f"now there is {choices}")
        print(players)

    if len(players) == 2:
        for id in players_id:
            member = await client.fetch_user(int(id))
            await member.send(f"{pc_choice}")
            await detective()
        if players[author] == "murder":
            @client.command()
            async def kill(ctx):
                await ctx.message.delete()
                killed = random.choice(list(players.values()))
                await ctx.send(f"{killed.mention} has been killed")
                killed.pop(players)
                killed.remove(players_id)
                await ctx.send(f"{players}")
        else:
            await ctx.send("you are not egiable to do this")

async def detective():
    if players[author] == "detective":
        ctx.send(f"{players}")

async def mur():
    if "murder" in players:
        choice = ["innocent","detective"]
        random.choice(choice)

async def dv():
    if "detective" in players:
        choice = "innocent"

client.run("token")
