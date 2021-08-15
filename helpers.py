import discord

from ranks import Rank

async def clear_channel(channel: discord.TextChannel, client: discord.Client):
    messages_in_channel = await channel.history().flatten()
    for message in messages_in_channel:
        if message.author == client.user:
            await message.delete()

def get_rank_banner_file(rank: Rank) -> discord.File:
    number_part = '0' + str(rank.value) if len(str(rank.value)) == 1 else rank.value
    abbreviation_part = rank.name
    return discord.File(f'./rank_banners/{number_part}_{abbreviation_part}.png')