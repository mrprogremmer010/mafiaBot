import discord
from discord.ext import commands
from discord.ext.tasks import loop
import random
import os



intents = discord.Intents(messages=True, guilds=True).all()
intents.members = True
client = commands.Bot(command_prefix = "!",intents = intents)
@loop(seconds=1)
async def chng_stat():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'mafia with {len(client.guilds)} servers'))


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
        await channel.send(f"{author} you enterd the game please wait for more {10-len(players)} players")
        await channel.send(f"now there is {choices}")
        print(players)

    if len(players) == 1:
        for id in players_id:
            member = await client.fetch_user(int(id))
            await member.send(f"{pc_choice}")

        if players[author] == "detective":
            await member.send(f"{players}")

        if players[author] == "murder":
            @client.command()
            async def kill(ctx):
                await ctx.message.delete()
                killed = random.choice(list(players.values()))
                killed_id = await client.fetch_user(int(id))
                await ctx.send(f"{killed.mention} has been killed")
                players.pop(killed)
                players_id.remove(killed_id)
                await ctx.send(f"{players}")
                if players[author] != "murder":
                    await member.send("you are not egiable to do this")
        if len(players) == 1:
            await ctx.send("oof the killer has won the game")
            players.clear()
            players_id.clear()
            
    @client.command()
    async def leave(ctx):
        await ctx.send("are you sure you want to leave? y/n")
        answer = await client.wait_for("message")
        if answer.content == "y":
            await ctx.send(f"{author} has been quit")
            players.pop(author)
            players_id.remove(author_id)
            play = " ".join(players.values())
            await channel.send(f"now there is {play}")
            return answer
        elif answer.content == "n":
            await ctx.send("ok we are glad you here")
            return answer
        if answer.author.mention != author:
            answer= await client.wait_for('message')
        elif answer.author.mention == author:
            massageStatus = False
        else:
            await ctx.send("invaild choice")
            answer = await client.wait_for("message")
        return answer







async def mur():
    if "murder" in players:
        choice = ["innocent","detective"]
        random.choice(choice)

async def dv():
    if "detective" in players:
        choice = "innocent"

client.run("NzkwOTY3NTI3MTE4MjA5MTA1.X-IT6Q.mxPjq3NKgLmwV93b3qePYH-rl9A")
