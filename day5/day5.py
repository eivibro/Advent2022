with open('input.txt') as f:
    lines = f.readlines()

def position_blank_line():
    i = 0
    iter = True
    while iter == True:
        if lines[i].__len__() > 1:
            if lines[i][1] == '1':
                iter = False
                length_longest = lines[i].__len__()
        i += 1
    return i, length_longest

def day5_one():
    blank_position = position_blank_line()
    storage = []
    for  i in range(1, blank_position[1]-1, 4):
        column = []
        for j in range(0,blank_position[0]-1):
            if lines[j][i].isalpha():
                column.append(lines[j][i])
        storage.append(column)
    
    for l in lines[blank_position[0]+1:lines.__len__()]:
        instructions = l.split()
        for k in range(0, int(instructions[1])):
            storage[int(instructions[5])-1].insert(0, \
                storage[int(instructions[3])-1].pop(0))
    print("".join([i[0] for i in storage]))

def day5_two():
    blank_position = position_blank_line()
    storage = []
    for  i in range(1, blank_position[1]-1, 4):
        column = []
        for j in range(0,blank_position[0]-1):
            if lines[j][i].isalpha():
                column.append(lines[j][i])
        storage.append(column)
    
    for l in lines[blank_position[0]+1:lines.__len__()]:
        instructions = l.split()
        crates = []
        for k in range(0, int(instructions[1])):
            crates.append(storage[int(instructions[3])-1].pop(0))
        for m in range(0, int(instructions[1])):
            storage[int(instructions[5])-1].insert(0, \
                crates.pop(-1))

    print("".join([i[0] for i in storage]))


day5_two()
