import re
import math

txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day6\input_test.txt",'r')

worksheet = []
text_backup = []

with txt:
    for line in txt:
        text_backup.append(line)
        row = []
        clean_ws = re.sub(r'\s+',' ',line).strip()
        row = re.split(r' ',clean_ws)
        row_int = []
        for x in row:
            try:
                row_int.append(int(x))
            except ValueError:
                row_int.append(x)
        worksheet.append(row_int)

problem_count = len(worksheet[0])
operand_count = len(worksheet)-1

print(text_backup)
text_backup.insert(operand_count, ' '*len(text_backup[0]))
print(text_backup)
transposed_text = [''.join(chars) for chars in zip(*text_backup)]
for line in transposed_text:
    print(line)
solutions = []

for problem in range(problem_count):
    factors = []
    for number in range(operand_count):
        factors.append(worksheet[number][problem])
    if worksheet[operand_count][problem] == "*":
        solutions.append(math.prod(factors))
    if worksheet[operand_count][problem] == "+":
        solutions.append(sum(factors))

print(f'Part 1 Solution: {sum(solutions)}')