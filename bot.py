import discord, os, random
from discord.ext import commands 

api_key = os.environ.get('topic-bot')
client = commands.Bot(command_prefix = '!')

beauty_topics = []

#Open and read file for topics related to beauty and add them to the list
with open('topics/beauty.txt') as f:
    for line in f:
        beauty_topics.append(line)


@client.event
async def on_ready():
    print('Bot is online!')

@client.command()
async def topic(ctx):
    idx = random.randrange(0, len(beauty_topics))
    topic_string = beauty_topics[idx]
    await ctx.send(topic_string)

client.run(api_key)

