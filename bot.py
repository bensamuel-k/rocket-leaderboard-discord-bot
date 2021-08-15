import os
import time

import discord

from playlists import Playlist
from ranks import Rank
from leaderboard import Leaderboard
from config import GUILD, TOKEN
from exceptions import EmptyRankException
from mock_players import mock_players, add_random_mock_player, update_random_mock_player_mmr

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
        await leaderboard_command(message, args)
    elif command == 'playlists':
        await playlists_command(message)
    elif command == 'ranks':
        await ranks_command(message)
    else:
        await message.channel.send(f'The command: **!{command}** does not exist.')

async def leaderboard_command(message: discord.Message, args: list):
    playlists = {
        '1s': Playlist.ONES,
        '2s': Playlist.TWOS,
        '3s': Playlist.THREES,
    }
    if len(args) > 0 and args[0] in playlists:
        playlist = playlists[args[0]]
        leaderboard = Leaderboard(client, playlist, message.channel)

        if len(args) > 1:
            rank = None
            for r in Rank:
                if r.name == args[1].upper():
                    rank = r
                    break
            if rank == None:
                await message.channel.send(f'The rank **{args[1]}** does not exist. Use !ranks for a list of rank abbreviations.')
            else:
                try:
                    await leaderboard.send_for_rank(rank)
                except EmptyRankException:
                    await message.channel.send(f'There are no players in **{rank.name}**.')
        else:
            await leaderboard.send(clear_channel=False)
    else:
        await message.channel.send('Syntax is: **!leaderboard playlist rank**. Specifying a **rank** is optional.\nUse **!playlists** and **!ranks** for possible values.')
    
async def playlists_command(message):
    await message.channel.send('Currently supported playlists are: **1s**, **2s**, **3s**.')

async def ranks_command(message):
    ranks_str = ''
    for rank in Rank:
        ranks_str += f'**{rank.name}**, '
    ranks_str = ranks_str[:-2]
    await message.channel.send(f'Possible rank abbreviations are: {ranks_str}.')

client.run(TOKEN)
