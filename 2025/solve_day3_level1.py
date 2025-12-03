def solve(f):
    total = 0
    for line in f:
        largest_ten="1"
        largest_ten_index=0
        largest_one="1"
        for index, num in enumerate(line[:-2]):
            if num > largest_ten:
                largest_ten=num
                largest_ten_index=index
        for num in line[largest_ten_index+1:-1]:
            if num > largest_one:
                largest_one=num
        total += int(largest_ten + largest_one)
    return total


with open("day_3.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_3.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)