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
            if invalid(curr):
                total += i
    return total

def invalid(input):
    input_len = len(input)
    for repeat_size in range(1, input_len//2 + 1):
        start = input[0:repeat_size]
        match = True
        for i in range(repeat_size, input_len, repeat_size):
            segment=input[i:i+repeat_size]
            if start != segment:
                match = False
                break
        if match:
            return True
    return False


with open("day_2.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_2.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)