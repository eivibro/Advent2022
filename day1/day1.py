with open('data_day1_1.txt') as f:
    lines = f.readlines()


# Calculate number of calories for the the elf that brought the most.
def day1_1():
    current = 0
    highest = 0
    for i in lines:
        if i != "\n":
            current += int(i)
        else:
            if current > highest:
                highest = current
            current = 0
    print(highest)


# Calculate number of calories for the the three elves that brought the most.
def day1_2():
    current = 0
    highest = [0, 0, 0]
    for k in lines:
        if k != "\n":
            current += int(k)
        else:
            highest.sort()
            if highest[0] < current:
                highest[0] = current
            current = 0
        highest.sort()
    if highest[0] < current:
        highest[0] = current
    print(sum(highest))


day1_2()
f.close()