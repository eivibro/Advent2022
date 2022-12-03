import string 

letters = list(string.ascii_letters)
values = range(1,53)
combined = dict(zip(letters, values))

with open('input.txt') as f:
    lines = f.readlines()

def find_item(line):
    half = int((len(line))/2)
    first_half = line[0:half]
    second_half = line[half:half*2]
    for i in first_half:
        for j in second_half:
            if i == j:
                return i

def day3_1():
    total = 0
    for l in lines:
        item = find_item(l)
        total += combined[item]
    print(total)

def find_badge(group):
    for i in group[0]:
        for j in group[1]:
            if j == i:
                for k in group[2]:
                    if j == k:
                        return j

def day3_taskTwo():
    x = range(0, int(len(lines)), 3)
    total = 0
    for i in x:
        total += combined[find_badge(lines[i:i+3])]
    print(total)

day3_taskTwo()
f.close()