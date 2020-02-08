import numpy as np
import random
import matplotlib.pyplot as plt

def bayInit():
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
    return bay


def findUrgentContainer(bay):
    min= np.size(bay)
    y = -1
    x = -1
    for i in range(0, np.size(bay, 0)):
        for j in range(0, np.size(bay,1)):
            if bay[i][j] < min and bay[i][j] > 0:
                y = i
                x = j
                min = bay[i][j]
    return y, x


def isMoveAble(bay, originalY, originalX):
    if originalY == 0:
        return True
    elif bay[originalY-1][originalX] != 0:
        return False
    else:
        return True


def moveContainer(bay, originalX, x, maxheight):
    topIndex = 2
    x = int(x)
    for i in reversed(range(0, maxheight+1)):
        if bay[i][originalX] != 0:
            topIndex = i
    temp = bay[topIndex][originalX]
    bay[topIndex][originalX] = 0
    topIndex = 2
    for i in reversed(range(0, maxheight+1)):
        if bay[i][x] != 0:
            topIndex = i-1
    bay[topIndex][x] = temp
    return topIndex


def isBayEmpty(bay):
    for i in range(0, len(bay)):
        for j in range(0, len(bay[0])):
            if bay[i][j] != 0:
                return False
    return True


def retrieveContainer(bay, y, x):
    bay[y][x] = 0


def R1(bay, x, maxHeight, maxWidth):
    satisfyR1 = np.array([])
    topindex = -1
    min = maxWidth - x
    index = -1
    for i in range(0, np.size(bay, 0)):
        if bay[i][x] != 0:
            topindex = i
            break
    for i in range(0,np.size(bay, 1)):
        bool = "yes"
        for j in range(0, np.size(bay, 0)):
            if bay[j][i] <= bay[topindex][x] and bay[j][i] != 0:
                bool = "no"
        if bay[maxHeight][i] == 0:
            bool = "no"
        if bool == "yes":
            satisfyR1 = np.append(satisfyR1, [i])

    for i in range(0, satisfyR1.size):
        if np.absolute(x - satisfyR1[i]) < min:
            min = np.absolute(x - satisfyR1[i])
            index = satisfyR1[i]
    return index


def R2(bay, x, maxHeight, maxWidth):
    satisfyR2 = np.array([])
    min = maxWidth - x
    index = -1
    for i in range(0, np.size(bay,1)):
        if bay[maxHeight][i] == 0:
            satisfyR2 = np.append(satisfyR2, [i])
    for i in range(0, satisfyR2.size):
        if np.absolute(x - satisfyR2[i]) < min:
            min = np.absolute(x - satisfyR2[i])
            index = satisfyR2[i]
    return index


def R3(bay, x, maxHeight, maxWidth):
    skylines = np.array([])
    index = -1
    min = maxWidth - x
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
        if np.absolute(x - i) < min and np.absolute(x - i) != 0:
            min = np.absolute(x - i)
            index = i
    return index


def R4(bay, x, maxHeight, maxWidth):
    satisfyR4 = np.array([])
    min = maxWidth - x
    index = -1
    for i in range(0, np.size(bay, 1)):
        if bay[0][i] == 0:
            satisfyR4 = np.append(satisfyR4, [i])
    for i in satisfyR4:
        if np.absolute(x - i) < min and np.absolute(x - i) != 0 :
            min = np.absolute(x - i)
            index = i
    return index


def generateChromosome():
    chromosome = []
    for i in range (0, 100):
        chromosome.append(random.randrange(1, 5))
    return chromosome


def getMaxWidth(bay):
    return len(bay[0])


def move(bay, chromosome, maxWidth):
    index = 0
    maxheight = 2
    moves = np.array([])
    while isBayEmpty(bay) == False:
        y, x = findUrgentContainer(bay)
        y = int(y)
        x = int(x)
        if isMoveAble(bay, y, x):
            retrieveContainer(bay, y, x)
        else:
            if chromosome[index] == 1 and R1(bay, x, maxheight, maxWidth) != None:
                i = int(R1(bay, x, maxheight, maxWidth))
                topIndex = moveContainer(bay, x, i, maxheight)
                moves = np.append(moves, [x, i, topIndex], axis=0)
            elif chromosome[index] == 2 and R2(bay, x, maxheight, maxWidth) != None:
                i = R2(bay, x, maxheight, maxWidth)
                topIndex = moveContainer(bay, x, i, maxheight)
                moves = np.append(moves, [x, i, topIndex], axis=0)
            elif chromosome[index] == 3 and R3(bay, x, maxheight, maxWidth) != None:
                i = R3(bay, x, maxheight, maxWidth)
                topIndex = moveContainer(bay, x, i, maxheight)
                moves = np.append(moves, [x, i, topIndex], axis=0)
            elif chromosome[index] == 4 and R4(bay, x, maxheight , maxWidth) != None:
                i = R4(bay, x, maxheight, maxWidth)
                topIndex = moveContainer(bay, x, i, maxheight)
                moves = np.append(moves, [x, i, topIndex], axis=0)
            index += 1

        """for i in range(0, np.size(bay, 0)):
            for j in range(0, np.size(bay, 1)):
                print(bay[i][j], end="   ")
            print("\n")
        print("\n")"""

    moves = np.reshape(moves, (int(moves.size/3), 3))
    return chromosome, moves, index


def calChromosomePool(bay, chromosomePool):
    maxWidth = getMaxWidth(bay)
    times = np.array([])

    for i in range(0, len(chromosomePool)):
        bay = bayInit()
        c, m, ind = move(bay, chromosomePool[i], maxWidth)
        moves.append([m])
        times = np.append(times, ind)
        chromosomePool.append([c])
    return chromosomePool, moves, times


def chromosomeSelect(times):
    middle = np.median(times)
    selectedIndexes = np.array([])
    for i in range(0, len(times)):
        if times[i] < middle:
            selectedIndexes = np.append(selectedIndexes, i)
    if selectedIndexes.size == 0:
        selectedIndexes = np.append(selectedIndexes, 0)
    return selectedIndexes

def crossover(indexes, chromosomePool):
    newChromosome = []
    #if len(chromosomePool) % 2 == 1:
    #   chromosomePool.append(chromosomePool[len(chromosomePool)])
    for i in range(0, int(indexes.size/2)):
        temp = chromosomePool[i][:int(len(chromosomePool[i])/2)]
        temp2 = chromosomePool[i+1][int(len(chromosomePool[i+1])/2):]
        temp = temp + temp2
        newChromosome.append(temp)
    return newChromosome


def GA():
    bay = bayInit()
    chromosomePool = []
    moves = []
    times = []
    indexes = np.array([])
    maxWidth = getMaxWidth(bay)

    for i in range (0, 1000):
        chromosomePool.append(generateChromosome())

    while len(chromosomePool) > 0:
        chromosomePool, moves, times = calChromosomePool(bay, chromosomePool)
        indexes = chromosomeSelect(times)
        chromosomePool = crossover(indexes, chromosomePool)
    return times[int(indexes)]


def RandomMoves() :
    bay = bayInit()
    chromosomePool = []
    moves = []
    times = []
    indexes = np.array([])
    maxWidth = getMaxWidth(bay)

    chromosomePool.append(generateChromosome())

    while len(chromosomePool) > 0:
        chromosomePool, moves, times = calChromosomePool(bay, chromosomePool)
        indexes = chromosomeSelect(times)
        chromosomePool = crossover(indexes, chromosomePool)
    return times


bay = bayInit()
chromosomePool = []
moves = []
times = []
indexes = np.array([])
maxWidth = getMaxWidth(bay)
GAtimes = []
"""for i in range(0, 500):
    times = np.append(times, RandomMoves())"""
"""print(np.average(times))"""
for i in range(0, 1000):
    GAtimes = np.append(GAtimes, GA())
    print(i)
print(np.average(GAtimes))
axes = plt.gca()
axes.set_ylim([3,35])
plt.plot(GAtimes)
plt.show()
