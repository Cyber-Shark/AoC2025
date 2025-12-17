import re

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day3\input.txt",'r')

joltage_list = []

with txt:
    for line in txt:
        first_digit = max(line[0:-2])
        first_index = line.index(first_digit)
        second_digit = max(line[first_index+1:-1])
        joltage = first_digit+second_digit
        joltage_list.append(joltage)


joltage_list_int = [int(x) for x in joltage_list]  
print(f'Part 1 Solution: {sum(joltage_list_int)}')