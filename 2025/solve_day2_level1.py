def solve(f):
    input = f.read()
    input = input.split(",")
    total = 0
    for values in input:
        values = values.split("-")
        start = int(values[0])
        end = int(values[1])
        for i in range(start, end+1):
            curr = str(i)
            curr_len = len(curr)
            halfpoint = int(curr_len/2)
            if curr_len % 2 == 0 and curr[:halfpoint] == curr[halfpoint:]:
                total += i
    return total

with open("day_2.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_2.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)