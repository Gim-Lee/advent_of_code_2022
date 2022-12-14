calories = [0]
with open('data/day1_input.txt') as file:
    for line in file:
        if line == '\n':
            calories.append(0)
            continue
        calories[-1] += (int(line.strip()))
print(sorted(calories)[-1])         # part1
print(sum(sorted(calories)[-3:]))   # part2