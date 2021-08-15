import os

import discord

from config import ONES_CHANNEL, TWOS_CHANNEL, THREES_CHANNEL, MIN_RANK, GUILD

from ranks import Rank
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
    player_occupied_ranks: list
    leaderboard_messages: dict

    def __init__(self, client: discord.Client, playlist: Playlist, channel: discord.TextChannel = None):
        self.playlist = playlist
        self.client = client

        self.players = mock_players

        if channel != None:
            self.channel = channel
        else:
            guild = discord.utils.get(client.guilds, name=GUILD)
            self.channel = discord.utils.get(guild.channels, name=channel_names[playlist])
        self.player_occupied_ranks = []
        self.leaderboard_messages = {}

    async def update(self):
        self.update_player_occupied_ranks()
        ranks_in_discord = list(self.leaderboard_messages.keys())

        self.player_occupied_ranks.sort(key=lambda rank: rank.value)
        ranks_in_discord.sort(key=lambda rank: rank.value)

        should_resend = self.player_occupied_ranks != ranks_in_discord

        if should_resend:
            await self.send()
        else:
            for rank, message in self.leaderboard_messages.items():
                await message.edit(content=self.get_message(rank))

    async def send(self, clear_channel=True):
        self.leaderboard_messages = {}
        if clear_channel:
            await helpers.clear_channel(self.channel, self.client)
        await self.channel.send(f'*{self.playlist.name.capitalize()} Leaderboard*')
        for rank in Rank:
            try:
                self.leaderboard_messages[rank] = await self.send_for_rank(rank)
            except EmptyRankException:
                if rank.name != MIN_RANK:
                    continue
            finally:
                if rank.name == MIN_RANK:
                    break

    async def send_for_rank(self, rank: Rank) -> discord.Message:
        message = self.get_message(rank)
        await self.channel.send(file=helpers.get_rank_banner_file(rank))
        return await self.channel.send(message)

    def get_message(self, rank: Rank) -> str:
        self.update_players
        players_in_rank = self.get_players_in_rank(rank)
        if (len(players_in_rank) == 0):
            raise EmptyRankException
        else:
            players_in_rank.sort(key=lambda player: player[self.playlist]['mmr'], reverse=True)
            result = '```\n'
            for player in players_in_rank:
                result += f"{player[self.playlist]['mmr']} {player['name']}\n"
            result += '```'
            return result

    def update_players(self):
        self.players = mock_players

    def update_player_occupied_ranks(self):
        self.update_players()
        for rank in Rank:
            players_in_rank = self.get_players_in_rank(rank)
            if len(players_in_rank) == 0 and rank in self.player_occupied_ranks:
                self.player_occupied_ranks.remove(rank)
            if len(players_in_rank) > 0 and rank not in self.player_occupied_ranks:
                self.player_occupied_ranks.append(rank)

    def get_players_in_rank(self, rank: Rank) -> list:
        return [player for player in self.players if player[self.playlist]['rank'] == rank]
