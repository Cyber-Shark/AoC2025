import re

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day5\input.txt",'r')

ranges_raw = []
ranges_int = []
ingredients = []
fresh_count = 0
fresh_ids = []

#extract ranges from input
with txt:
    for line in txt:
        search_res = re.search(r'\d+-\d+', line)
        if search_res is not None:
            ranges_raw.append(search_res.group(0))
        else:
            number = re.search(r'\d+', line)
            if number is not None:
                ingredients.append(int(number.group()))


#convert to list of tuples and int
for item in ranges_raw:
    low, high = re.split(r'-',item)
    span = [int(low), int(high)]
    ranges_int.append(span)

def fresh_check(item, fresh_ranges):
    fresh = False
    for line in fresh_ranges:
        if item >= line[0] and item <= line[1]:
            fresh = True
            break
        else:
            fresh = False
    return fresh

"""for line in ranges_int:
    for item in range(line[0], line[1]+1):
        fresh_ids.append(item)
    print('line done')"""

for item in ingredients:
    if fresh_check(item, ranges_int):
        fresh_count += 1




ranges_combine = sorted(ranges_int)

range_merge_found = True
while range_merge_found == True:
    range_merge_found = False
    for i in range(len(ranges_combine)-1):
        if ranges_combine[i][1] >= ranges_combine[i+1][0]: #element2 overlaps with element 1's range
            range_merge_found = True
            if ranges_combine[i][1] <= ranges_combine[i+1][1]:
                ranges_combine[i][1] = ranges_combine[i+1][1]
            del ranges_combine[i+1]
            break


all_id_count = 0
for item in ranges_combine:
    span = item[1] - item[0] + 1
    all_id_count += span


print(f'Part 1 Solution: {fresh_count}')
print(f'Part 2 Solution: {all_id_count}')