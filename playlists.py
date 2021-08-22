from enum import Enum
from config import ONES_CHANNEL, TWOS_CHANNEL, THREES_CHANNEL
class Playlist(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3

channel_names = {
    Playlist.ONES: ONES_CHANNEL,
    Playlist.TWOS: TWOS_CHANNEL,
    Playlist.THREES: THREES_CHANNEL,
}