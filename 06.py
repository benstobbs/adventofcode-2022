def unique(x):
    for char in x:
        if x.count(char) > 1:
            return False
    return True

s = open("06_input.txt").read().replace("\n", "")
for n_unique in [4, 14]:
    for i in range(n_unique, len(s)):
        if unique(s[i-n_unique:i]):
            print(i)
            break
