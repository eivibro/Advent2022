with open('test_input.txt') as f:
    lines = f.readlines()

def first_blank(lines):
    row = 0
    for l in lines:
        if l == "\n":
            print("Test")