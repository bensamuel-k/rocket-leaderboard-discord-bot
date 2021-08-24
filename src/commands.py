import discord

from playlists import Playlist
from leaderboard import Leaderboard
from ranks import Rank
from exceptions import EmptyRankException

playlist_abbreviations = {
    '1s': Playlist.ONES,
    '2s': Playlist.TWOS,
    '3s': Playlist.THREES,
}

async def leaderboard(client: discord.Client, message: discord.Message, args: list):
    if len(args) > 0 and args[0] in playlist_abbreviations:
        playlist = playlist_abbreviations[args[0]]
        leaderboard = Leaderboard(client, playlist, message.channel)

        if len(args) > 1:
            rank = None
            for r in Rank:
                if r.name == args[1].upper():
                    rank = r
                    break
            if rank == None:
                await message.channel.send(f'The rank **{args[1]}** does not exist. Use **!ranks** for a list of rank abbreviations.')
            else:
                try:
                    await leaderboard.send_for_rank(rank)
                except EmptyRankException:
                    await message.channel.send(f'There are no players in **{rank.name}**.')
        else:
            await leaderboard.send(clear_channel=False)
    else:
        await message.channel.send('Syntax is: **!leaderboard playlist rank**. Specifying a rank is optional.\nUse **!playlists** and **!ranks** for possible values.')
    
async def playlists(message):
    await message.channel.send('Currently supported playlists are: **1s**, **2s**, **3s**.')

async def ranks(message):
    ranks_str = ''
    for rank in Rank:
        ranks_str += f'**{rank.name}**, '
    ranks_str = ranks_str[:-2]
    await message.channel.send(f'Possible rank abbreviations are: {ranks_str}.')
