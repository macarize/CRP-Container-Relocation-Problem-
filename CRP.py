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

def moveContainer(bay, originalWidth, originalHeight, width, height):
    temp = bay[originalWidth][originalHeight]
    bay[originalWidth][originalHeight] = 0

    bay[height][width] = temp

def R1(bay, width, height, maxHeight):
    satisfyR1 = np.array([])
    topindex = -1
    for i in range(0, np.size(bay, 0)):
        if bay[i][width] != 0:
            topindex = i
            break
    print(topindex)
    for i in range(0,np.size(bay, 1)):
        bool = "yes"
        print('outer', i)
        for j in range(0, np.size(bay, 0)):
            if bay[j][i] <= bay[topindex][width] and bay[j][i] != 0 :
                bool = "no"
            print("inner", j)
        if bool == "yes":
            satisfyR1 = np.append(satisfyR1, [i])

        print(satisfyR1)
    for i in range(0, satisfyR1.size):
        min = 100
        if np.absolute(width - i) < min:
            min = np.absolute(width - i)
    return satisfyR1[min]

i, j = findUrgentContainer(bay)
print(i, j)
print(R1(bay, 2, 2, 2))

