import pytz
from os import environ as env

YEAR           = 2022
SESSION_COOKIE = env["SESSION_COOKIE"]
LEADERBOARD    = env["LEADERBOARD"]
URL            = f"https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD}.json"
DISCORD_TOKEN  = env["DISCORD_TOKEN"]
COMMAND_PREFIX = '!'
UTC = pytz.timezone('UTC')
EST = pytz.timezone('US/Eastern')
