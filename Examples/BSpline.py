import matplotlib.pyplot as plt
from math import pow
import numpy as np


def geta(t, a=0):
    return 1 / 2 * pow(t - a, 2)


def getb(t, b=0):
    return 3 / 4 - pow(t - b - 1.5, 2)


def getc(t, c=0):
    return 1 / 2 * pow(t - c - 3, 2)


def getPt(p0, p1, p2, a, b, c):
    return c * p0 + b * p1 + a * p2


if __name__ == '__main__':
    # labels
    xShift = 0.9
    yShift = 1.1
    fsize = 12

    # points
    px = np.array([0, 2, 4, 5])
    py = np.array([0, 2, 1, 3])
    for i in range(0, px.__len__()):
        plt.text(px[i] * xShift, py[i] * yShift, "p" + str(i), fontsize=fsize)
    plt.plot(px, py, '--o')

    ptx = []
    pty = []

    # [2 , 3]-------------------------------------------------------------------
    for t in np.arange(0.25, 1, 0.25, dtype=float):
        ptx.append(getPt(px[0], px[1], px[2], geta(t, a=2), getb(t, b=1), getc(t, c=0)))
        pty.append(getPt(py[0], py[1], py[2], geta(t, a=2), getb(t, b=1), getc(t, c=0)))
        plt.text(ptx[ptx.__len__() - 1] * xShift, pty[pty.__len__() - 1] * yShift, "pt1_" + str(t), fontsize=fsize)

    # [3 , 4]-------------------------------------------------------------------
    for t in np.arange(0.25, 1, 0.25, dtype=float):
        ptx.append(getPt(px[1], px[2], px[3], geta(t, a=3), getb(t, b=2), getc(t, c=1)))
        pty.append(getPt(py[1], py[2], py[3], geta(t, a=3), getb(t, b=2), getc(t, c=1)))
        plt.text(ptx[ptx.__len__() - 1] * xShift, pty[pty.__len__() - 1] * yShift, "pt2_" + str(t), fontsize=fsize)
    # plot-----------------------------------------------------------------------
    plt.plot(ptx, pty, '--o')

    plt.show()