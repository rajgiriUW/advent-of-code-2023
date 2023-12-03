path = r'C:\Users\Raj\Dropbox\UW Work\aoc_2023'
day = '02'

file = open(path + r'\\' + day + '.txt')
data = [x.strip() for x in file.readlines()]

import math

ids = []

for d in data:
    counts = {'red': [], 'green': [], 'blue': []}
    
    game, rules = d.split(':')
    gameid = int(game.split('Game ')[1])
    
    rules = [x.strip() for x in rules.split(';')]

    for r in rules:
        colors = r.split(',')
        for c in colors:
            count = c.split(' ')
            counts[count[-1]].append(int(count[-2]))
    
    if max(counts['red'])<=12 and max(counts['green'])<=13 and max(counts['blue'])<=14:
        ids.append(gameid)
        
print('Part 1:', sum(ids))

# Part 2:
# I think my setup for part 1 allows me to do Part 2

ids = []

for d in data:
    counts = {'red': [], 'green': [], 'blue': []}
    
    game, rules = d.split(':')
    gameid = int(game.split('Game ')[1])
    
    rules = [x.strip() for x in rules.split(';')]

    for r in rules:
        colors = r.split(',')
        for c in colors:
            count = c.split(' ')
            counts[count[-1]].append(int(count[-2]))
    
    powers = [max(counts['red']), max(counts['green']), max(counts['blue'])]
    ids.append(math.prod(powers))
    
print('Part 2:', sum(ids))