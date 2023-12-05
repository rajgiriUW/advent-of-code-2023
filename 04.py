path = r'C:\Users\Raj\Dropbox\UW Work\aoc_2023'
day = '04'

file = open(path + r'\\' + day + '.txt')
data = [x.strip() for x in file.readlines()]

import re
import numpy as np

# Part 1
points = 0
for d in data:
    _d = [x.strip() for x in d.split(':')[1:]]
    _d[0] = _d[0] + ' ' # for regex searching below
    winners, numbers = _d[0].split('|')
    winners = [int(x) for x in re.findall('\d+\s', winners)]
    numbers = [int(x) for x in re.findall('\d+\s', numbers)]

    # Use set intersection to find the points
    matches = set(winners).intersection(set(numbers))
    if any(matches):
        points += 2** (len(matches)-1)

print('Part 1:', points)

# Part 2
def evalgame(game):
    _d = [x.strip() for x in game.split(':')[1:]]
    _d[0] = _d[0] + ' ' # for regex searching below
    winners, numbers = _d[0].split('|')
    winners = [int(x) for x in re.findall('\d+\s', winners)]
    numbers = [int(x) for x in re.findall('\d+\s', numbers)]

    # Use set intersection to find the points
    matches = set(winners).intersection(set(numbers))
    
    return len(matches)

games = np.ones(len(data), dtype=int) # Each game evaluated once

# Count matches; the next N games count the current game number
for n, d in enumerate(data):
        
    matches = evalgame(d)
    games[np.arange(n+1,n+1+matches)] += games[n]

print('Part 2:', sum(games))