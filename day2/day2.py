with open('input.txt') as f:
    lines = f.readlines()

scores = {'X': 1, 'Y': 2, 'Z': 3}

def day2_1():
    scores = {'X': 1, 'Y': 2, 'Z': 3}
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
    scores = {'X': 1, 'Y': 2, 'Z': 3}
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
    choice = ''
    letter_l = line[0]
    letter_r = line[2]
    letters = ['X', 'Y', 'Z']
    position = {'A': 0, 'B': 1, 'C': 2}
    if letter_r == 'X':
        return(letters[(position[letter_l]+2)%3])
    elif letter_r == 'Y':
        return(letters[(position[letter_l])])
    elif letter_r == 'Z':
        return(letters[(position[letter_l]+1)%3])


day2_2()
f.close()         