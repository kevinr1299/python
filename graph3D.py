from mpl_toolkits.mplot3d import Axes3D
from sympy import Symbol, diff, limit, oo
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import os
import re

# Define function


def clear(): return os.system('cls')


def draw():
    try:
        print('Enter M:')
        xval = parseInput('np')
        print('Enter N:')
        yval = parseInput('np')
        print('Enter P:')
        zval = parseInput('np')
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x, y, z = np.meshgrid(np.arange(-5, 5, 1),
                              np.arange(-5, 5, 1),
                              np.arange(-5, 5, 1))
        M = eval(xval)
        N = eval(yval)
        P = eval(zval)
        ax.quiver(x, y, z, M, N, P, length=0.5, normalize=True)
        plt.show()
    except:
        print('Misspelled equations')


def partial():
    try:
        x = Symbol('x')
        y = Symbol('y')
        z = Symbol('z')
        print('Enter M:')
        M = parseInput('sym')
        print('Enter N:')
        N = parseInput('sym')
        print('Enter P:')
        P = parseInput('sym')
        my = diff(eval(M), y)
        nx = diff(eval(N), x)
        mz = diff(eval(M), z)
        px = diff(eval(P), x)
        nz = diff(eval(N), z)
        py = diff(eval(P), y)
        print('dM/dy = {0}'.format(my))
        print('dN/dx = {0}'.format(nx))
        print('dM/dz = {0}'.format(mz))
        print('dP/dx = {0}'.format(px))
        print('dN/dz = {0}'.format(nz))
        print('dP/dy = {0}'.format(py))
        if (my == nx and mz == px and nz == py):
            print('The field is conservative')
        else:
            print('The field not is conservative')
    except:
        print('Misspelled equations')
    input("Press Enter to continue...")


def lim():
    try:
        x = Symbol('x')
        print('Enter general term:')
        an = parseInput('sym')
        result = limit(eval(an), x, oo)
        print('Lim {0} = {1}'.format(an, result))
    except:
        print('Misspelled equations')
    input("Press Enter to continue...")


def parseInput(prefix):
    value = input()
    sinValue = re.sub('sin', prefix + '.sin', value)
    cosValue = re.sub('cos', prefix + '.cos', sinValue)
    tanValue = re.sub('tan', prefix + '.tan', cosValue)
    sqrtValue = re.sub('sqrt', prefix + '.sqrt', tanValue)
    parseValue = re.sub(r'\^', '**', sqrtValue)
    return parseValue


try:
    opt = 0
    while opt != '4':
        clear()
        print('1. Calculate if the field is conservative')
        print('2. Draw the field')
        print('3. Calculate limit')
        print('4. Go out')
        print('Select option:')
        opt = input()
        if eval(opt) == 1:
            partial()
        elif eval(opt) == 2:
            draw()
        elif eval(opt) == 3:
            lim()
        elif eval(opt) == 4:
            print('Good bye!!')
        else:
            print('Option not found')
except:
    print('Error executing')
