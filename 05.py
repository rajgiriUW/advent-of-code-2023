path = r'C:\Users\Raj\Dropbox\UW Work\aoc_2023'
day = '05'

file = open(path + r'\\' + day + '_unittest.txt')
data = [x.strip() for x in file.readlines() if x != '\n']

import numpy as np

# Populate a Dictionary
keys = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

df = {}
for k in keys:
    df[k] = []
seeds = [int(x) for x in data[0].split(' ')[1:]]

# Rules dictionary
for d in data[1:]:

    # is a map
    if 'map' in d:
        
        srckey = d.split('-')[0]
        dstkey = d.split('-')[2].split(' ')[0]

        continue
    
    # is a rule. Go through each number and assign
    dest, src, rng = [int(x) for x in d.split(' ')]
    df[dstkey].append([dest, src, rng])


def mapseed(seed):
    
    loc = seed
    for key in keys:
        
        for rule in df[key]: # go through each rule
            dest, src, rng = rule
            
            if loc >= src and loc <= src + rng:
                
                idx = loc - src 
                loc = dest + idx
                break
    
    return loc

# Go through each seed    
vals = list(map(mapseed, seeds))
    
print('Part 1:', min(vals))

# Part 2
# Was stuck, looked a bit to see how others did this...

seeds = np.reshape(seeds, [len(seeds)//2, 2]) # convert to ranges
vals = []

for seedrng in seeds:
    
    vals.append(list(map(mapseed, [seedrng[0], seedrng[0]+seedrng[1]])))

low = vals - seeds #relative change for each incoming seed

