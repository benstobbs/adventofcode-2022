scores = {"A":1, "B":2, "C":3}
rtol = {"X":"A", "Y":"B", "Z":"C"}
what_beats_what = {"A":"C", "B":"A", "C":"B"}

score = 0

for line in open("02_input.txt"):
    [you, me] = line.replace("\n", "").split(" ")
    me = rtol[me]

    score += scores[me]

    if me == you:
        score += 3
    elif what_beats_what[me] == you:
        score += 6

print(score)