from ranks import Rank
from playlists import Playlist

mock_players = [
    {
        'name': 'playerA',
        Playlist.ONES: {
            'mmr': 1256,
            'rank': Rank.GC2
        },
        Playlist.TWOS: {
            'mmr': 1830,
            'rank': Rank.GC3
        },
        Playlist.THREES: {
            'mmr': 1906,
            'rank': Rank.SSL
        }
    },
    {
        'name': 'playerB',
        Playlist.ONES: {
            'mmr': 1190,
            'rank': Rank.GC1
        },
        Playlist.TWOS: {
            'mmr': 1813,
            'rank': Rank.GC3
        },
        Playlist.THREES: {
            'mmr': 1925,
            'rank': Rank.SSL
        }
    },
]
