def solve(f):
    total = 0
    for line in f:
        val = largest_12_num(line.strip())
        total += int(val)
    return total

def largest_12_num(line):
    largest_12_num=[]
    previous_largest_index=0
    for place in range(12,0,-1):
        largest_current=line[previous_largest_index]
        largest_current_index=0
        for index, num in enumerate(line[previous_largest_index:len(line)-place+1]):
            if num > largest_current:
                largest_current=num
                largest_current_index=index
        largest_12_num.append(largest_current)
        previous_largest_index+=largest_current_index+1
    return "".join(largest_12_num)

with open("day_3.sample", "r") as f:
    sample_sol = solve(f)
    print("sample:", sample_sol)

with open("day_3.input", "r") as f:
    sol = solve(f)
    print("solution:", sol)