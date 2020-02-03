import numpy as np

bay = np.zeros((3, 7), dtype=int)

bay[0][3] = 9
bay[0][5] = 8
bay[1][0] = 6
bay[1][0] = 6
bay[1][2] = 5
bay[1][3] = 7
bay[1][5] = 11
bay[2][0] = 10
bay[2][1] = 2
bay[2][2] = 1
bay[2][3] = 3
bay[2][5] = 4

def findUrgentContainer(bay):
    min= 0
    height = 0
    width = 0
    for i in range(0, np.size(bay, 0)):
        for j in range(0, np.size(bay,1)):
            if bay[i][j] != 0:
                min = bay[i][j]
                break
    for i in range(0, np.size(bay, 0)):
        for j in range(0, np.size(bay,1)):
            if bay[i][j] < min and bay[i][j] > 0:
                height= i
                width = j
                min = bay[i][j]
    return height, width
def isMoveAble(bay, originalWidth, originalHeight):
    if originalHeight == 0:
        return True
    elif bay[originalHeight-1][originalWidth] != 0:
        return False
    else:
        True
def moveContainer(bay, originalWidth, originalHeight, width, height):
    temp = bay[originalWidth][originalHeight]
    bay[originalWidth][originalHeight] = 0

    bay[height][width] = temp
def isBayEmpty(bay):
    for i in range(0, len(bay)):
        for j in range(0, len(bay[0])):
            if bay[i][j] != 0:
                return False
    return True
def R1(bay, width, maxHeight):
    satisfyR1 = np.array([])
    topindex = -1
    min = 6 - width
    index = -1
    for i in range(0, np.size(bay, 0)):
        if bay[i][width] != 0:
            topindex = i
            break
    for i in range(0,np.size(bay, 1)):
        bool = "yes"
        for j in range(0, np.size(bay, 0)):
            if bay[j][i] <= bay[topindex][width] and bay[j][i] != 0:
                bool = "no"
        if bay[maxHeight][i] == 0:
            bool = "no"
        if bool == "yes":
            satisfyR1 = np.append(satisfyR1, [i])

    for i in range(0, satisfyR1.size):
        if np.absolute(width - satisfyR1[i]) < min:
            min = np.absolute(width - satisfyR1[i])
            index = satisfyR1[i]
    return index

def R2(bay, width, maxHeight):
    satisfyR2 = np.array([])
    min = 6 - width
    index = -1
    for i in range(0, np.size(bay,1)):
        if bay[maxHeight][i] == 0:
            satisfyR2 = np.append(satisfyR2, [i])
    for i in range(0, satisfyR2.size):
        if np.absolute(width - satisfyR2[i]) < min:
            min = np.absolute(width - satisfyR2[i])
            index = satisfyR2[i]
    return index

def R3(bay, width, maxHeight):
    skylines = np.array([])
    index = -1
    min = 6 - width
    for i in range(0, np.size(bay, 1)):
        index = 2
        for j in range(0, np.size(bay, 0)):
            if bay[j][i] != 0:
                index = j
                break
        skylines = np.append(skylines, [maxHeight-index])
    minimum = np.amin(skylines)
    indices = [i for i, v in enumerate(skylines) if v == minimum]
    for i in indices:
        if np.absolute(width - i) < min and np.absolute(width - i) != 0:
            min = np.absolute(width - i)
            index = i
    return index
def R4(bay, width, maxHeight):
    satisfyR4 = np.array([])
    min = 6 - width
    index = -1
    for i in range(0, np.size(bay, 1)):
        if bay[0][i] == 0:
            satisfyR4 = np.append(satisfyR4, [i])
    for i in satisfyR4:
        if np.absolute(width - i) < min and np.absolute(width - i) != 0 :
            min = np.absolute(width - i)
            index = i
    return index

i, j = findUrgentContainer(bay)
print(i, j)
print(R1(bay, 2, 2))
print(R2(bay, 2, 2))
print(R3(bay, 2, 2))
print(R4(bay, 2, 2))