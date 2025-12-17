import re

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day1\input.txt",'r')

position  = 50
position_list =[]
zero_list = []
zero_count = 0

def rotate_count(position,command):
    direction = re.search(r'\D', command).group()
    quantity = int(re.search(r'\d+', command).group())
    step_zero = 0
    if direction == "R":
        new_position = (position + quantity) % 100
        step_zero = (position + quantity)//100

    if direction == "L":
        new_position = (position - quantity) % 100
        if position > 0 and (position - quantity) <= 0:
            step_zero += 1
        step_zero += abs(position - quantity)//100
    
    return new_position, step_zero

with txt:
    for line in txt:
        position, step_zero = rotate_count(position,line)
        position_list.append(position)
        zero_count += step_zero


zero_list = [item for item in position_list if item == 0]


print(f'Part 1 Solution: {len(zero_list)}')
print(f'Part 2 Solution: {zero_count}')