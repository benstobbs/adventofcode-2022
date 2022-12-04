in_common = lambda lines: [char for char in lines[0] if char in lines[1] and char in lines[2]][0]

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("03_input.txt") as f:
    lines = f.read().split("\n")
    
    print(sum([
        priority.index(in_common(lines[i*3:i*3+3]))+1
        for i in range(int(len(lines)/3))
    ]))
