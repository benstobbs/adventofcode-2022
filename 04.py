overlaps_p1 = lambda a, b, c, d: int(a) <= int(c) and int(b) >= int(d)
overlaps_p2 = lambda a, b, c, d: int(c) <= int(b) and int(d) >= int(a)

pairs = [[x.split("-") for x in line.replace("\n", "").split(",")] for line in open("04_input.txt")]

for comp in [overlaps_p1, overlaps_p2]:
    print(sum([
        1 if comp(a, b, c, d) or comp(c, d, a, b) else 0
        for [[a, b], [c, d]] in pairs
    ]))
