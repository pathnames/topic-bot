import discord, pathlib, random, os
from discord.ext import commands 

api_key = os.environ.get('topic-bot')
client = commands.Bot(command_prefix = '!')

#Global variables for topics:
# beauty_topics = []
# morality_topics = []
topics = []

# #Open and read file for topics related to beauty and add them to the list
# with open('topics/beauty.txt') as f:
#     for line in f:
#         beauty_topics.append(line)

# #Open and read file for topics related to morality and add them to the list
# with open('topics/morality.txt') as f:
#     for line in f:
#         morality_topics.append(line)

#Open and write each line of each file in the topics directory:
for path in pathlib.Path('topics').iterdir():
    with open(path, mode = 'r') as f:
        for line in f:
            topics.append(line)
    
@client.event
async def on_ready():
    print('Bot is online!')

# @client.command()
# async def btopic(ctx):
#     idx = random.randrange(0, len(beauty_topics))
#     topic_string = beauty_topics[idx]
#     await ctx.send(topic_string)

@client.command()
async def topic(ctx):
    idx = random.randrange(0, len(topics))
    topic_string = topics[idx]
    await ctx.send(topic_string)

client.run(api_key)

