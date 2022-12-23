from pylab import *

with open('input.txt') as f:
    lines = f.readlines()

data = zeros((lines[0].__len__() - 1, lines.__len__()))

for i in range(0, lines[0].__len__()-1):
    for j in range(0, lines.__len__()):
        data[i, j] = int(lines[i][j])

def checkTree(i, j, row, column):
    tree = row[j]
    hidden = [False, False, False, False]
    for e in row[0:j]:
        if e >= tree:
            hidden[0] = True
    for e in row[j+1:]:
        if e >= tree:
            hidden[1] = True
    for e in column[i+1:]:
        if e >= tree:
            hidden[2] = True
    for e in column[0:i]:
        if e >= tree:
            hidden[3] = True
    for b in hidden:
        if b == False:
            return 0
    return 1

def checkView(i, j, row, column):
    science_score = 1
    tree = row[j]
    direction_view = zeros(4)
    for e in row[j+1:]:
        if e < tree:
            direction_view[0] += 1
        else:
            direction_view[0] += 1
            break
    for e in flip(row[:j]):
        if e < tree:
            direction_view[1] += 1
        else:
            direction_view[1] += 1
            break
    for e in column[i+1:]:
        if e < tree:
            direction_view[2] += 1
        else:
            direction_view[2] += 1
            break
    for e in flip(column[0:i]):
        if e < tree:
            direction_view[3] += 1
        else:
            direction_view[3] += 1
            break
    for s in direction_view:
        science_score *= s
    return science_score

total_trees = data[0, :].__len__()*data[:, 0].__len__()
total_hidden = 0
maxScience = 0
for i in range(1, data[0,:].__len__() - 1):
    for j in range(1, data[:,0].__len__() - 1):
        total_hidden += checkTree(i, j, data[i, :], data[:, j])
        science_score = checkView(i, j, data[i, :], data[:, j])
        if science_score > maxScience:
            maxScience = science_score

print(maxScience)


