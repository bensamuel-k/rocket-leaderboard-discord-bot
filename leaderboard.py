import os

import discord

from config import ONES_CHANNEL, TWOS_CHANNEL, THREES_CHANNEL, MIN_RANK, GUILD

from ranks import Rank, rank_emojis, rank_names
from playlists import Playlist
from mock_players import mock_players
from exceptions import EmptyRankException
import helpers 

channel_names = {
    Playlist.ONES: ONES_CHANNEL,
    Playlist.TWOS: TWOS_CHANNEL,
    Playlist.THREES: THREES_CHANNEL,
}


class Leaderboard:
    playlist: Playlist
    client: discord.Client
    channel: discord.TextChannel

    players: list
    leaderboard_message: discord.Message

    def __init__(self, client: discord.Client, playlist: Playlist, channel: discord.TextChannel = None):
        self.playlist = playlist
        self.client = client

        self.players = mock_players

        if channel != None:
            self.channel = channel
        else:
            guild = discord.utils.get(client.guilds, name=GUILD)
            self.channel = discord.utils.get(guild.channels, name=channel_names[playlist])
        self.leaderboard_message = None

    async def update(self):
        if (not self.leaderboard_message):
            raise Exception('there is no leaderboard_message to update yet. send() needs to be called at least once before update()')
        message = self.get_leaderboard()
        await self.leaderboard_message.edit(content=message)

    async def send(self, clear_channel=True):
        if clear_channel:
            await helpers.clear_channel(self.channel, self.client)
        message = self.get_leaderboard()
        self.leaderboard_message = await self.channel.send(message)

    async def send_for_rank(self, rank: Rank):
        message = f'*{self.playlist.name.capitalize()} Leaderboard*\n{self.get_leaderboard_for_rank(rank)}'
        await self.channel.send(message)

    def get_leaderboard(self) -> str:
        message = f'*{self.playlist.name.capitalize()} Leaderboard*\n\n'
        for rank in Rank:
            try:
                message += f'{self.get_leaderboard_for_rank(rank)}\n'
            except EmptyRankException:
                if rank.name != MIN_RANK:
                    continue
            finally:
                if rank.name == MIN_RANK:
                    break
        return message[:-1]

    def get_leaderboard_for_rank(self, rank: Rank) -> str:
        self.update_players
        players_in_rank = self.get_players_in_rank(rank)
        if (len(players_in_rank) == 0):
            raise EmptyRankException
        else:
            players_in_rank.sort(key=lambda player: player[self.playlist]['mmr'], reverse=True)

            result = f'{rank_emojis[rank]} {rank_names[rank]}\n```\n'
            for player in players_in_rank:
                result += f"{player[self.playlist]['mmr']} {player['name']}\n"
            result += '```'
            return result

    def update_players(self):
        self.players = mock_players

    def get_players_in_rank(self, rank: Rank) -> list:
        return [player for player in self.players if player[self.playlist]['rank'] == rank]
