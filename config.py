import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')
ONES_CHANNEL = os.getenv('CHANNEL_NAME_ONES')
TWOS_CHANNEL = os.getenv('CHANNEL_NAME_TWOS')
THREES_CHANNEL = os.getenv('CHANNEL_NAME_THREES')
MIN_RANK = os.getenv('MIN_RANK')
