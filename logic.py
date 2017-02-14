import statlist
import random

player_stats = {stat: 0 for stat in statlist.stats}

for i in range(5):
    player_stats[random.choice(statlist.stats)] += random.randint(1, 3)

def get_significant_stats(n):
    stats = list(player_stats.items())
    stats.sort(key=lambda stat: abs(stat[1]), reverse=False)
    return stats[-n:][::-1]


def currently_available_options():
    return ["beta", "gamma", "delta", "alpha"]


def process_option(option, add_line):
    add_line(option)
