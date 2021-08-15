import os

import discord

from playlists import Playlist
from ranks import Rank
from leaderboard import send_leaderboard, update_leaderboard
from config import GUILD, TOKEN
from mock_players import mock_players

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild = discord.utils.get(client.guilds, name=GUILD)

    leaderboard_messages = await send_leaderboard(Playlist.THREES, guild, client)
    mock_players[0][Playlist.THREES] = {'mmr': 1820, 'rank': Rank.GC3}
    await update_leaderboard(leaderboard_messages, Playlist.THREES, guild, client)

client.run(TOKEN)
