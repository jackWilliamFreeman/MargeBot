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
        await message.channel.send('Lisa Needs Braces')

    if 'total war'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        await message.channel.send('You need at least sixteen pigs to finish the job in one sitting, so be wary of any man who keeps a pig farm. ... That means that a single pig can consume two pounds of uncooked flesh every minute. Hence the expression, "as greedy as a pig"')

    if 'brace for the charge'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        await message.channel.send('What difference does it make to the dead, the orphans and the homeless, whether the mad destruction is wrought under the name of totalitarianism or in the holy name of liberty or democracy?')


    if not message.guild:
        await message.channel.send('not today mate')

async def get_cleaned_splits(message_content):
    splits = message_content.split('-')
    cleaned_splits = []
    for split in splits:
        cleaned_splits.append(split.strip())
    return cleaned_splits

client.run(os.getenv('MARGE_TOKEN'))
