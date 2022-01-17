import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello {0}!'.format(message.author))
TOKEN = 'OTMyNjE4MjA4Njg5NjY0MDIw.YeVmZA.xW8hSU_UN9MZluyVJIjhCTF9dmM'
client.run(TOKEN)