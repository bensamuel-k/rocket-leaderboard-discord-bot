# rocket-leaderboard-discord-bot

currently this uses mock player data because psyonix does not give away api keys. maybe i will write a bakkesmod plugin later which could track and send mmr to the leaderboard for each individual player.

## setup

upload the .png files inside **./rl_ranks** as emojis to your guild

clone repo
```
git clone git@github.com:bensamuel-k/rocket-leaderboard-discord-bot.git
```

switch to repo directory
```
cd rocket-leaderboard-discord-bot
```

create new file .env and fill with contents of .env.example
```
cat .env.example > .env
```

use text editor to change at least the value of DISCORD_TOKEN and GUILD_NAME
```
nano .env
```

install dependencys from requirements.txt
```
python3 -m pip3 install -r requirements.txt
```

start bot
```
python3 ./src/bot.py
```
