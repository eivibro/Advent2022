with open('input.txt') as f:
    lines = f.readlines()

def day4_1():
    total = 0
    for i in lines:
        parts = i.split(",")
        numbers = [int(parts[0].split("-")[0]), int(parts[0].split("-")[1]), \
            int(parts[1].split("-")[0]), int(parts[1].split("-")[1])]
        if numbers[0] == numbers[2]:
            total += 1
        elif numbers[0] <= numbers[2]:
            if numbers[1] >= numbers[3]:
                total += 1
        else:
            if numbers[1] <= numbers[3]:
                total += 1
    print(total)

def day4_two():
    total = 0
    for i in lines:
        parts = i.split(",")
        numbers = [int(parts[0].split("-")[0]), int(parts[0].split("-")[1]), \
            int(parts[1].split("-")[0]), int(parts[1].split("-")[1])]
        if numbers[3] < numbers[0]:
            total += 1
        elif numbers[1] < numbers[2]:
            total += 1
        elif numbers[0] > numbers[3]:
            total += 1
        elif numbers[2] > numbers[3]:
            total += 1
    print(len(lines)-total)


day4_two()
f.close()