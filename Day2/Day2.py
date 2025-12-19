import re

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day2\input_test.txt",'r')

id_list = []
number_count = 0
invalid_list = []

with txt:
    for line in txt:
        id_list = re.split(r',',line)

def range_splitter(text_range):
    range_low, range_high = re.split(r'-',text_range)
    #print(f'low: {range_low}, high: {range_high}')
    return range_low, range_high

def range_checker_double(range_low,range_high):
    global invalid_list
    for number in range(int(range_low), int(range_high)+1):
        s = str(number)
        whole_len = len(s)
        half_len = whole_len//2
        if whole_len%2 == 0 and s[:half_len] == s[-half_len:]:
            invalid_list.append(s)

#to-do: solve for general case
#notice pattern in string indices, and floor division number
def range_checker_all(range_low,range_high):
    global invalid_list
    for number in range(int(range_low), int(range_high)+1):
        s = str(number)
        digits = len(s)
        if digits >= 2: #one digit repeat case
            if s == s[0]*digits:
                if s not in invalid_list:
                    invalid_list.append(s)
        if digits >= 4: #two digit repeat case
            if s == s[0:2]*(digits//2):
                if s not in invalid_list:
                    invalid_list.append(s)
        if digits >= 6: #three digit repeat case
            if s == s[0:3]*(digits//3):
                if s not in invalid_list:
                    invalid_list.append(s)
        if digits >= 8: #three digit repeat case
            if s == s[0:4]*(digits//4):
                if s not in invalid_list:
                    invalid_list.append(s)
        if digits >= 10: #three digit repeat case
            if s == s[0:5]*(digits//5):
                if s not in invalid_list:
                    invalid_list.append(s)


for item in id_list:
    range_checker_all(*range_splitter(item))

invalid_list_int = [int(x) for x in invalid_list]    
print(f'Part 1 Solution: {sum(invalid_list_int)}')