scores = {"A":1, "B":2, "C":3}
# rtol = {"X":"A", "Y":"B", "Z":"C"}
what_beats_what = {"A":"C", "B":"A", "C":"B"}

score = 0

for line in open("02_input.txt"):
    [you, outcome] = line.replace("\n", "").split(" ")
    
    if outcome == "Y":
        me = you
    elif outcome == "X":
        me = what_beats_what[you]
    else:
        options = ["A", "B", "C"]
        options.remove(you)
        options.remove(what_beats_what[you])
        me = options[0]

    score += scores[me]

    if me == you:
        score += 3
    elif what_beats_what[me] == you:
        score += 6

print(score)