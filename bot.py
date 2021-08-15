import os

import discord

from playlists import Playlist
from ranks import Rank
from leaderboard import Leaderboard
from config import GUILD, TOKEN
from mock_players import mock_players

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    threes_leaderboard = Leaderboard(client, Playlist.THREES)

    await threes_leaderboard.send()
    mock_players[0][Playlist.THREES] = {'mmr': 1820, 'rank': Rank.GC3}
    await threes_leaderboard.update()

client.run(TOKEN)
