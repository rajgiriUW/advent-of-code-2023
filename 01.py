path = r'C:\Users\Raj\Dropbox\UW Work\aoc_2023'
day = '01'

import re

file = open(path + r'\\' + day + '.txt')
data = [x for x in file.readlines()]

total = 0
for d in data:
    
    lt = re.search('[0-9]', d)
    rt = re.search('[0-9]', d[::-1])
    
    lt = d[lt.span()[0]]
    rt = d[::-1][rt.span()[0]]
    
    total += int(lt+rt)
    
print('Part 1:', total)

# Part 2

numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
           'six':6, 'seven':7, 'eight':8, 'nine':9}

def min_text(d):

    left = None
    right = None
    leftpos = None
    rightpos = None    

    # left-to-right    
    leftpos = 9999999
    for n in numbers.keys():
        
        xpos = re.search(n, d)
        
        if xpos: #if found
            if xpos.span()[0] < leftpos:
                left = numbers[n]
                leftpos = xpos.span()[0]
    
    # right-to-left
    rightpos = 9999999
    d = d[::-1]
    for n in numbers.keys():
        
        n = n[::-1]
        xpos = re.search(n, d)
        
        if xpos: 
            if xpos.span()[0] < rightpos:
                right = numbers[n[::-1]]
                rightpos = xpos.span()[0]   
    
    return left, leftpos, right, rightpos

total = 0
for d in data:
    
    # Numbers
    lt = re.search('[0-9]', d)
    rt = re.search('[0-9]', d[::-1])
    ltpos = lt.span()[0]
    rtpos = rt.span()[0]
    
    lt = d[lt.span()[0]]
    rt = d[::-1][rt.span()[0]]
    
    left, leftpos, right, rightpos = min_text(d)
    
    if left:
       if leftpos < ltpos:
           lt = left
    if right:
        if rightpos < rtpos:
            rt = right
    
    total += int(str(lt)+str(rt))
    
print('Part 2', total)