lines = open("05_input.txt").read().split("\n")

stack_names_line = [idx for idx, line in enumerate(lines) if line[:2] == " 1"][0]
max_stack_number = max([int(n) for n in lines[stack_names_line].split(" ") if n != ""])
stack_cols = [lines[stack_names_line].find(str(i)) for i in range(1, max_stack_number+1)]

def p1(stacks, n, fromm, to):
    for _ in range(n):
        stacks[to-1].append(stacks[fromm-1].pop())

def p2(stacks, n, fromm, to):
    stacks[to-1].extend(stacks[fromm-1][-n:])
    for _ in range(n):
        stacks[fromm-1].pop()

for fn in [p1, p2]:
    # list of lists, top of stack at end
    stacks = [[line[stack_col] for line in lines[stack_names_line-1::-1] if line[stack_col] != " "] for stack_col in stack_cols]

    for line in lines[stack_names_line+2:]:
        [n, fromm, to] = [int(char) for char in line.replace("move", "").replace("from", "").replace("to", "").split(" ") if char != ""]
        fn(stacks, n, fromm, to)

    print("".join([stack[-1] for stack in stacks]))