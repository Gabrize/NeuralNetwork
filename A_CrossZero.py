import matplotlib.pyplot as plt
import matplotlib.patches as patch

import numpy as np

minEl = 0
maxEl = 1

xSize = 4
ySize = 4


def matrixIsAcceptable(elements, maxX, maxY):
    print(elements)
    zeroAm = 0
    oneAm = 0
    # Проверка по горизонтали
    for y in range(0, maxY):
        checkedEl = elements[y][0]
        isDivised = True
        for x in range(0, maxX):
            if elements[y][x] == 0:
                zeroAm += 1
            elif elements[y][x] == 1:
                oneAm += 1

            if (elements[y][x] != checkedEl):
                isDivised = False

        if isDivised:
            print('is divesed')
            return False

    print('zeroAm = ', zeroAm)
    print('oneAm = ', oneAm)

    if not zeroAm == oneAm == 8:
        print('is not equal')
        return False

    # Проверка по вертикали
    for x in range(0, maxX):
        checkedEl = elements[0][x]
        isDivised = True
        for y in range(1, maxY):
            if (elements[y][x] != checkedEl):
                isDivised = False
        if isDivised:
            print('is divised')
            return False

    return not isDivised

if __name__ == '__main__':

    elements = np.random.randint(minEl, maxEl + 1, size=(ySize, xSize))
    while not matrixIsAcceptable(elements, xSize, ySize):
        elements = np.random.randint(minEl, maxEl + 1, size=(ySize, xSize))
        print('----------------------------------')


    plt.xlim(0,4)
    plt.ylim(0,4)

    rect = patch.Rectangle((0, 0),1, 1, color='r', fill=True)

    plt.gca().add_patch(rect)

    plt.show()