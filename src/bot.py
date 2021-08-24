import time

import discord

from playlists import Playlist
from leaderboard import Leaderboard
from config import TOKEN
from mock_players import add_random_mock_player, update_random_mock_player_mmr
import commands

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for i in range (10):
        add_random_mock_player(str(i))
        
    threes_leaderboard = Leaderboard(client, Playlist.THREES)
    await threes_leaderboard.send()

    while True:
        time.sleep(10)
        for i in range (10):
            update_random_mock_player_mmr(Playlist.THREES)
        await threes_leaderboard.update()

@client.event
async def on_message(message):
    if message.author == client.user or message.content[0] != '!' or message.content == '!':
        return
    message_parts = message.content[1:].split()
    command = message_parts[0]
    args = message_parts[1:]

    if command == 'leaderboard':
        await commands.leaderboard(client, message, args)
    elif command == 'playlists':
        await commands.playlists(message)
    elif command == 'ranks':
        await commands.ranks(message)

client.run(TOKEN)
