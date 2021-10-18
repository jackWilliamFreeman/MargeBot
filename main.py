import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)
guild_name = 'MWM'
members = ''

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await get_members()


async def get_members():
    for guild in client.guilds:
        if guild.name == guild_name:
            break
    global members
    members = guild.members

@client.event
async def on_message(message):
    #channel = client.get_channel(812906949124423700)
    if message.author == client.user:
        return

    if 'dental plan'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        print('Encouraging Drinking')
        await message.channel.send('Lisa Needs Braces')

    if not message.guild:
        await message.channel.send('not today mate')

async def get_cleaned_splits(message_content):
    splits = message_content.split('-')
    cleaned_splits = []
    for split in splits:
        cleaned_splits.append(split.strip())
    return cleaned_splits

client.run(os.getenv('TOKEN'))
