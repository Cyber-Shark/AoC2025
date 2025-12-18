import re

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day3\input_test.txt",'r')

joltage_list = []

"""with txt:
    for line in txt:
        first_digit = max(line[0:-2])
        first_index = line.start(first_digit)
        second_digit = max(line[first_index+1:-1])
        joltage = first_digit+second_digit
        joltage_list.append(joltage)"""

with txt:
    for line in txt:
        joltage = ''
        start = 0
        print(f'Number {line[0:-1]}')
        for frame in reversed(range (1,13)): #increased range by 1 to account for \n char at end
            digit = max(line[start:-frame])
            start = line[start:-frame].index(digit)
            joltage += line[start]
            
        print(f'Joltage: {joltage}\n')
        joltage_list.append(joltage)

joltage_list_int = [int(x) for x in joltage_list]  
print(f'Part 1 Solution: {sum(joltage_list_int)}')