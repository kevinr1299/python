from mpl_toolkits.mplot3d import Axes3D
from sympy import Symbol, diff, limit, oo
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import signal
import math
import os
import re

# Define function


def clear(): return os.system('cls')


def draw():
    try:
        print('Enter M: ', end='')
        xval = parseInput('np')
        print('Enter N: ', end='')
        yval = parseInput('np')
        print('Enter P: ', end='')
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
        print('Enter M: ', end='')
        M = parseInput('sym')
        print('Enter N: ', end='')
        N = parseInput('sym')
        print('Enter P: ', end='')
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
        serie = ''
        print('Enter the limit: ', end='')
        t = input()
        top = eval(t)
        print('Enter general term(x): ', end='')
        an = parseInput('math')
        if isinstance(top, int):
            for i in range(1, top + 1):
                if i != 1:
                    serie += ' + '
                exp = re.sub('x', str(i), an)
                expValue = calcualteFactorial(exp)
                serie += str(eval(expValue))
            print('Σ({0}) = {1} = {2}'.format(an, serie, eval(serie)))
        elif t == 'oo':
            i = 1
            print('Σ({0}) ='.format(an), end='')
            while True:
                exp = re.sub('x', str(i), an)
                expValue = calcualteFactorial(exp)
                result = round(eval(expValue), 8)
                print(' {0} +'.format(result), end='')
                i += 1
        else:
            print('The limit of the series must be an integer or infinity')
    except:
        print('Misspelled equations')
    input("Press Enter to continue...")


def parseInput(prefix):
    value = input()
    sinValue = re.sub('sin', prefix + '.sin', value)
    cosValue = re.sub('cos', prefix + '.cos', sinValue)
    tanValue = re.sub('tan', prefix + '.tan', cosValue)
    sqrtValue = re.sub('sqrt', prefix + '.sqrt', tanValue)
    if (prefix == 'sym'):
        piValue = re.sub('pi', 'math.pi', sqrtValue)
    else:
        piValue = re.sub('pi', prefix + '.pi', sqrtValue)
    facValue = calcualteFactorial(piValue)
    parseValue = re.sub(r'\^', '**', facValue)
    return parseValue


def calcualteFactorial(value):
    try:
        resultFactorial = value
        searchFactorial = re.findall(r'\d+!', value)
        for factorial in searchFactorial:
            integer = re.search(r'\d+', factorial)
            init = eval(integer.group(0))
            result = 1
            for i in range(1, init + 1):
                result *= i
            resultFactorial = re.sub(factorial, str(result), resultFactorial)
        return resultFactorial
    except:
        print('Error calculating the factorial')


try:
    opt = 0
    while opt != '4':
        clear()
        print('1. Calculate if the field is conservative')
        print('2. Draw the field')
        print('3. Calculate series')
        print('4. Go out')
        print('Select option: ', end='')
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
