import discord

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_message(message):
    if str(message.author) == "Ri0ee#8401":
        if "my boi" in message.content.lower():
            await message.channel.send('PRAISE!')

        if "self-destruct, please" == message.content.lower():
            await message.channel.send('OK, MASTER!')
            await client.close()


client.run(token)