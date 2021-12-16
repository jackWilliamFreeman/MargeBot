import discord
import os
import random

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
    if message.author == client.user:
        return

    if 'dental plan'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        if random.randint(0,100) < 5:
            await message.reply('You think you know about pain? \
Talk to my second wife. She does. Or she thinks she does. \
She says that once when she was nineteen or twenty she got between a couple of cats fighting – her own cat and a neighbor’s – and one of them went at her, climbed her like a tree, tore gashes out of her thighs and breasts and belly that you still can see today, scared her so badly she fell back down her again, all tooth and claw and spitting fury. Thirty-six stitches I think she said she got. And a fever that lasted days. \
My second wife says that’s pain. \
She doesn’t know shit, that woman. My existence is pain')
        else:
            await message.channel.send('Lisa Needs Braces')

    if 'total war'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        await message.channel.send('Lisa needs to brace for the charge!')

    if not message.guild:
        await message.channel.send('not today mate')

async def get_cleaned_splits(message_content):
    splits = message_content.split('-')
    cleaned_splits = []
    for split in splits:
        cleaned_splits.append(split.strip())
    return cleaned_splits

client.run(os.getenv('MARGE_TOKEN'))
