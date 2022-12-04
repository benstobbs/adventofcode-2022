def in_common(line):
    mp = int(len(line)/2)
    for char in line[:mp]:
        if char in line[mp:]:
            return char

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("03_input.txt") as f:
    print(sum([priority.index(in_common(line.replace("\n", "")))+1 for line in f]))        