x = 1
xs = [] # xs are values of x after each cycle (xs[0] is x after cycle 1)
for line in open("10_input.txt").read().split("\n"):
    if line[:4] == "noop":
        xs.append(x)
    else:
        xs.append(x)
        x += int(line.split(" ")[-1])
        xs.append(x)

print(sum([xs[i-2]*i for i in range(20, 221, 40)]))

for i, x in enumerate([1] + xs[:-1]):
    print(
        "#" if i % 40 in [x-1, x, x+1] else ".",
        end="\n" if i % 40 == 39 else ""
    )