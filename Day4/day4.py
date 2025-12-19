txt = open(r"C:\Users\ddamschen\OneDrive - Inventprise\Documents\AdventOfCode2025\Day4\input.txt",'r')

grid = []

with txt:
    for line in txt:
        line = line.replace("@", "1")
        line = line.replace(".", "0")
        row = []
        for character in line:
            if character != '\n':
                row.append(character)
        grid.append(row)

total_columns = len(grid[0])
total_rows = len(grid)

#build "moat" of 0s around dataset
for item in grid:
    item.insert(0,"0")
    item.append("0")
zero_row = ["0"] * (total_columns+2)

grid.insert(0, zero_row)
grid.append(zero_row)

#update space
total_columns = len(grid[0])
total_rows = len(grid)

adjacent_list = []

change_made = True

while change_made == True:
    change_made = False
    for rows in range(1,total_rows-1):
        for columns in range (1, total_columns-1):
            if grid[rows][columns] == "1":
                slots = []
                slots.append(grid[rows-1][columns-1])
                slots.append(grid[rows-1][columns])
                slots.append(grid[rows-1][columns+1])
                slots.append(grid[rows][columns-1])
                slots.append(grid[rows][columns+1])
                slots.append(grid[rows+1][columns-1])
                slots.append(grid[rows+1][columns])
                slots.append(grid[rows+1][columns+1])
                slots_int = [int(x) for x in slots] 
                adjacent = sum(slots_int)
                if adjacent < 4:
                    grid[rows][columns] = "0"
                    change_made = True
                adjacent_list.append(adjacent)

accesible = 0
for item in adjacent_list:
    if item < 4:
        accesible += 1

grid_int = [[int(item) for item in row] for row in grid]

print(f'Part 1/2 solution: {accesible}')