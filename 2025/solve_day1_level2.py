def solve(f):
    new_val = 50
    dial = 50
    total = 0
    for line in f:
        op = line[0]
        val = int(line[1:-1])
        #print(dial, line[:-1])
        if op == "L":
            new_val = dial - val
        if op == "R":
            new_val = dial + val
        
        #print("new_val:", new_val)
        if new_val < 0:
            click = abs(new_val) // 100
            click += 1
            if dial == 0:
                click -= 1
            #print("clicks:", click)
        elif new_val > 0:
            click = new_val // 100
            #print("clicks:", click)
        elif new_val == 0:
            click = 1
            #print("click:", click)
        #print()

        total += click
        dial = new_val % 100
    return total

with open("day_1.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_1.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)