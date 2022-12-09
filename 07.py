SIZES = []
class Directory():
    def __init__(self):
        self.children = []
    def size(self):
        global SIZES
        size = sum([child.size() if isinstance(child, Directory) else child for _, child in self.children.items()])
        SIZES.append(size)
        return size

path = []
root = Directory()

for cmd in open("07_input.txt").read().split("$"):
    if cmd[:3] == " cd":
        dir = cmd.replace(" cd", "").replace(" ", "").replace("\n", "")
        if dir == "/":
            pass
        elif dir == "..":
            path.pop()
        else:
            path.append(dir)
    elif cmd[:3] == " ls":
        cwd = root
        for p in path:
            cwd = cwd.children[p]
        
        cwd.children = dict([
            (y, Directory()) if x == "dir" else (y, int(x))
            for [x, y] in [item.split(" ") for item in cmd.split("\n")[1:] if item != ""]
        ])

total = root.size()
print(sum([size for size in SIZES if size < 100000])) # P1
print(sorted([size for size in SIZES if  70000000 - total + size >= 30000000])[0])