with open('test_input.txt') as f:
    lines = f.readlines()

line_changed = False
storage = []
for l in lines:
    if line_changed == False:
        for i in l:
            print(i)