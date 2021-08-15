import discord

async def clear_channel(channel: discord.TextChannel, client: discord.Client):
    messages_in_channel = await channel.history().flatten()
    for message in messages_in_channel:
        if message.author == client.user:
            await message.delete()