with open('input.txt') as f:
    text = f.readline()

def check_group(group, found):
    length = group.__len__()
    if length > 1:
        for i in range(1,length):
            if group[0] == group[i]:
                return False
        return(check_group(group[1:], found))
    else:
        found = True
    return(found)

def day6_one():
    for i in range(0,text.__len__()-3):
        if check_group(text[i:i+4], False) == True:
            print(i+4)
            break

def day6_two():
    for i in range(0,text.__len__()-3):
        if check_group(text[i:i+14], False) == True:
            print(i+14)
            break

day6_one()
day6_two()