import discord
from discord.ext import commands
from discord.ext.tasks import loop
import random
import os

from dotenv import load_dotenv
load_dotenv()

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



@client.command()
async def join(ctx):
    players_id = []
    players = {}
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
        await channel.send(f"{author} you are on the game please wait for more {10-len(players)} players")
        await channel.send(f"now there is {choices}")

    if len(players) == 2:
        for id in players_id:
            member = await client.fetch_user(author_id)
            await member.send(f"{pc_choice}")
    if players[author] == "murder":
        @client.command()
        async def kill(ctx):
            await ctx.message.delete()
            killed = random.choice(players)
            await ctx.send(f"{killed.mention} has been killed")
            killed.remove(players)
            killed.remove(players_id)
            print(players)
    else:
        await ctx.send("you are not egiable to do this")

    @client.command()
    async def vote(ctx, member: discord.Member):
        count = 0
        othercount = 0


    if players[author] == "detective":
        @client.command()
        async def km(ctx, member: discord.Member):
            pass



client.run(os.getenv('BOT_TOKEN'))
