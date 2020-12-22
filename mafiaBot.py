import discord
from discord.ext import commands

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
            channel = await user_id.create_dm()
            await channel.send(f"{random.choice(choice)}")
        @client.command()
        async def kill(ctx):
            await ctx.message.delete()
            await ctx.send(f"{words}".format((words)))









client.run("NzkwOTY3NTI3MTE4MjA5MTA1.X-IT6Q.hy940SLSGZeYBMoKkoXyNLoFO5A")
