with open('input.txt') as f:
    lines = f.readlines()

scores = {'X': 1, 'Y': 2, 'Z': 3}

def day2_1():
    total = 0
    for l in lines:
        total += scores[l[2]] 
        if l[0] == 'A':
            if l[2] == 'X':
                total += 3
            elif l[2] == 'Y':
                total += 6
        elif l[0] == 'B':
           if l[2] == 'Z':
               total += 6
           elif l[2] == 'Y':
               total += 3
        elif l[0] == 'C':
          if l[2] == 'X':
              total += 6
          elif l[2] == 'Z':
              total += 3
    print(total)                  
                  
                  
def day2_2():
    total = 0
    choice = '' 
    for l in lines:
        choice = choose(l)
        total += scores[choice]
        if l[0] == 'A':
            if choice == 'X':
                total += 3
            elif choice == 'Y':
                total += 6
        elif l[0] == 'B':
           if choice == 'Z':
               total += 6
           elif choice == 'Y':
               total += 3
        elif l[0] == 'C':
          if choice == 'X':
              total += 6
          elif choice == 'Z':
              total += 3
    print(total)      


def choose(line):
    letters = ['X', 'Y', 'Z']
    position = {'A': 0, 'B': 1, 'C': 2}
    if line[2] == 'X':
        return(letters[(position[line[0]]+2)%3])
    elif line[2] == 'Y':
        return(letters[(position[line[0]])])
    elif line[2] == 'Z':
        return(letters[(position[line[0]]+1)%3])


day2_2()
f.close()         