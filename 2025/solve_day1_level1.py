def solve(f):
    dial = 50
    total = 0
    for line in f:
        op = line[0]
        val = int(line[1:-1])
        if op == "L":
            dial = dial - val
        if op == "R":
            dial = dial + val
        dial = dial % 100
        if dial == 0:
            total += 1
    return total

with open("day_1.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_1.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)