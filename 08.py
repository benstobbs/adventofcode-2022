grid = open("08_input.txt").read().split("\n")

side_visible = lambda side, height: sum([tree >= height for tree in side]) == 0
visible = 0

max_score = 0
def side_scenic(side, height):
    for i, tree in enumerate(side):
        if tree >= height:
            return i+1
    return len(side)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        sides = [
            list(grid[y][:x])[::-1],
            list(grid[y][x+1:]),
            [row[x] for row in grid[:y]][::-1],
            [row[x] for row in grid[y+1:]]
        ]

        if sum([side_visible(side, grid[y][x]) for side in sides]) > 0:
            visible += 1

        score = 1
        for side in sides:
            score *= side_scenic(side, grid[y][x])
        max_score = max([score, max_score])

print(visible)
print(max_score)