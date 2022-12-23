with open('input.txt') as f:
    lines = f.readlines()

class dir:
    def __init__(self, name):
        self.name = name
        self.children_dirs = {}
        self.size = 0
        self.parent = self
        
    def calculateSize(self):
        for d in self.children_dirs:
            self.size += self.children_dirs[d].calculateSize()
        return self.size

def day7_one():
    size = 0
    for d in dirs:
        if d.size <= 100000:
            size += d.size
    print(size)

def day7_two():
    free = 7e7 - root.size
    needed = 3e7
    delete_at_least = needed - free
    oldSmallest = dirs[0]
    for d in dirs:
        if d.size >= delete_at_least and d.size < oldSmallest.size:
            oldSmallest = d
    print(oldSmallest.size)

root = dir("/")
current = root
dirs = []
dirs.append(current)
for l in lines[1:]:
    split = l.split()
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] != "..":
                current = current.children_dirs[split[2]]
            else:
                current = current.parent
    elif split[0] == "dir":
        current.children_dirs[split[1]] = dir(split[1])
        dirs.append(current.children_dirs[split[1]])
        current.children_dirs[split[1]].parent = current
    else:
        current.size += int(split[0])

root.calculateSize()

day7_two()