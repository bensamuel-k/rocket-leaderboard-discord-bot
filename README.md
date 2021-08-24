# rocket-leaderboard-discord-bot

the images in **./rl_ranks** need to be uploaded as emojis in your discord guild and the following environment variables need to be set:

* DISCORD_TOKEN={your-bots-token}
* GUILD_NAME={name-of-the-guild}
* CHANNEL_NAME_ONES={channel-name-for-ones-leaderboard}
* CHANNEL_NAME_TWOS={channel-name-for-twos-leaderboard}
* CHANNEL_NAME_THREES={channel-name-for-threes-leaderboard}
* MIN_RANK={abbrevation-for-minimal-rank-to-be-shown-on-leaderboard}

rank-abbreviations are the names of the elements in the **Rank** enum inside **./src/ranks.py**

currently this also uses mock player data because psyonix does not give away api keys. maybe i will write a bakkesmod plugin later which could track and send mmr to the leaderboard for each individual player.
