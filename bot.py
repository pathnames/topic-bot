import discord, pathlib, random, os
from discord.ext import commands 

api_key = os.environ.get('topic-bot')
client = commands.Bot(command_prefix = '!')

#Array to hold all the topics:
topics = []


#Open and write each line of each file in the topics directory:
for path in pathlib.Path('topics').iterdir():
    with open(path, mode = 'r') as f:
        for line in f:
            topics.append(line)
    
@client.event
async def on_ready():
    print('Bot is online!')

@client.command()
async def topic(ctx):
    idx = random.randrange(0, len(topics))
    topic_string = topics[idx]
    await ctx.send(topic_string)

client.run(api_key)

