elves = []
s = 0

for line in open("01_input.txt"):
    if line == "\n":
        elves.append(s)
        s = 0
    else:
        s += int(line.replace("\n", ""))

elves.sort(reverse=True)
print("Part 1:", elves[0])
print("Part 2:", sum(elves[:3]))