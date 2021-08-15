import random
import time

from ranks import Rank
from playlists import Playlist

def update_random_mock_player_mmr(playlist: Playlist):
    random_player_index = random.choice(range(len(mock_players)))
    new_mmr = mock_players[random_player_index][playlist]['mmr'] + random.choice([9, -9])
    mock_players[random_player_index][playlist] = {'mmr': new_mmr, 'rank': get_rank(new_mmr)}

def get_rank(mmr: int) -> Rank:
    for rank in list(mock_rank_distribution.keys()):
        if rank == Rank.SSL: 
            if mmr >= mock_rank_distribution[Rank.SSL]['lower']:
                return Rank.SSL
        elif rank == Rank.B1:
            if mmr < mock_rank_distribution[Rank.B1]['upper']:
                return Rank.B1
        else:
            if mmr in range(mock_rank_distribution[rank]['lower'], mock_rank_distribution[rank]['upper']):
                return rank

def add_random_mock_player(player_index: str):
    ones_mmr = random.choice(range(0, 2500))
    twos_mmr = random.choice(range(0, 2500))
    threes_mmr = random.choice(range(0, 2500))
    mock_players.append(
        {
            'name': 'player' + player_index,
            Playlist.ONES: {
                'mmr': ones_mmr,
                'rank': get_rank(ones_mmr) 
            },
            Playlist.TWOS: {
                'mmr': twos_mmr,
                'rank': get_rank(twos_mmr)
            },
            Playlist.THREES: {
                'mmr': threes_mmr,
                'rank': get_rank(threes_mmr)
            }
        }
    )

mock_players = []

mock_rank_distribution = {
    Rank.SSL: {'lower': 1857},
    Rank.GC3: {'lower': 1706, 'upper': 1857},
    Rank.GC2: {'lower': 1560, 'upper': 1706},
    Rank.GC1: {'lower': 1435, 'upper': 1560},
    Rank.C3: {'lower': 1213, 'upper': 1435},
    Rank.C2: {'lower': 1080, 'upper': 1213},
    Rank.C1: {'lower': 1003, 'upper': 1080},
    Rank.D3: {'lower': 923, 'upper': 1003},
    Rank.D2: {'lower': 843, 'upper': 923},
    Rank.D1: {'lower': 778, 'upper': 843},
    Rank.P3: {'lower': 715, 'upper': 778},
    Rank.P2: {'lower': 655, 'upper': 715},
    Rank.P1: {'lower': 598, 'upper': 655},
    Rank.G3: {'lower': 534, 'upper': 598},
    Rank.G2: {'lower': 478, 'upper': 535},
    Rank.G1: {'lower': 442, 'upper': 478},
    Rank.S3: {'lower': 389, 'upper': 442},
    Rank.S2: {'lower': 320, 'upper': 389},
    Rank.S1: {'lower': 238, 'upper': 320},
    Rank.B3: {'lower': 154, 'upper': 238},
    Rank.B2: {'lower': 55, 'upper': 154},
    Rank.B1: {'upper': 54},
}

