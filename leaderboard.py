import os

import discord

from config import ONES_CHANNEL, TWOS_CHANNEL, THREES_CHANNEL, MIN_RANK

from ranks import Rank
from playlists import Playlist
from mock_players import mock_players
from exceptions import EmptyRankException
from helpers import clear_channel

non_empty_ranks = []

async def update_leaderboard(leaderboard_messages: dict, playlist: Playlist, guild: discord.Guild, client: str):
    update_non_empty_ranks(playlist)
    ranks_in_discord = list(leaderboard_messages.keys())
    non_empty_ranks.sort(key=lambda rank: rank.value)
    ranks_in_discord.sort(key=lambda rank: rank.value)
    should_resend = non_empty_ranks != ranks_in_discord

    if should_resend:
        await send_leaderboard(playlist, guild, client)
    else:
        for rank, message in leaderboard_messages.items():
            await message.edit(content=get_leaderboard_message(rank, playlist))

async def send_leaderboard(playlist: Playlist, guild: discord.Guild, client: discord.Client) -> dict:
    channel_name = ONES_CHANNEL if playlist == Playlist.ONES else TWOS_CHANNEL if playlist == Playlist.TWOS else THREES_CHANNEL
    channel = discord.utils.get(guild.channels, name=channel_name)
    await clear_channel(channel, client)

    channel_name = ONES_CHANNEL if playlist == Playlist.ONES else TWOS_CHANNEL if playlist == Playlist.TWOS else THREES_CHANNEL
    channel = discord.utils.get(guild.channels, name=channel_name)

    leaderboard_messages = {}
    await channel.send(f'*{playlist.name.capitalize()} Leaderboard*')
    for rank in Rank:
        if rank.name == MIN_RANK:
            break
        try:
            leaderboard_messages[rank] = await send_leaderboard_for_rank(rank, playlist, channel)
        except EmptyRankException:
            continue

    return leaderboard_messages

async def send_leaderboard_for_rank(rank: Rank, playlist: Playlist, channel: discord.channel.TextChannel) -> discord.Message:
    leaderboard_message = get_leaderboard_message(rank, playlist)
    rank_banner = get_rank_banner(rank)

    await channel.send(file=rank_banner)
    return await channel.send(leaderboard_message)

def get_rank_banner(rank: Rank) -> discord.File:
    number_part = '0' + str(rank.value) if len(str(rank.value)) == 1 else rank.value
    abbreviation_part = rank.name
    return discord.File(f'./rank_banners/{number_part}_{abbreviation_part}.png')

def get_leaderboard_message(rank: Rank, playlist: Playlist) -> str:
    players = mock_players
    players_in_rank = [player for player in players if player[playlist]['rank'] == rank]
    if (len(players_in_rank) == 0):
        raise EmptyRankException
    else:
        players_in_rank.sort(key=lambda player: player[playlist]['mmr'], reverse=True)
        result = '```\n'
        for player in players_in_rank:
            result += f"{player[playlist]['mmr']} {player['name']}\n"
        result += '```'
        return result
    
def update_non_empty_ranks(playlist: Playlist):
    players = mock_players
    for rank in Rank:
        players_in_rank = [player for player in players if player[playlist]['rank'] == rank]
        if len(players_in_rank) == 0 and rank in non_empty_ranks:
            non_empty_ranks.remove(rank)
        if len(players_in_rank) > 0 and rank not in non_empty_ranks:
            non_empty_ranks.append(rank)

