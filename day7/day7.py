with open('test_input.txt') as f:
    lines = f.readlines()

class dir:
    def __init__(self, name):
        self.name = name
        self.children_dirs = {}
        self.size = 0

root = dir("/")
over = root
for l in lines[1:]:
    split = l.split()
    if split[0] == '$':
        if split[0] == "dir":
            over.children_dirs
        elif split[1] == "cd":
            if split[2] != "..":
                over
                dirs[dir_position].children_dirs.append(dirs[dir_position+1])
                dir_position += 1
            else:
                dir_position -= 1
    elif split[0] != "dir" and split[0]:
        dirs[dir_position].size += int(split[0])

dirnum = 0
print(dirs[dirnum].name)
print(dirs[dirnum].size)
print(dirs[dirnum].children_dirs)
