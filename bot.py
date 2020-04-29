import discord, os
from discord.ext import commands 

api_key = os.environ.get('topic-bot')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is online!')

@client.command()
async def topic(ctx):
    await ctx.send("Sending new topic!")



client.run(api_key)

