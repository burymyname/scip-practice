#!/usr/bin/env python3

'''
Exercise 1.8: 
    Newton's method for cube roots is based on the fact 
    that if y is an approximation to the cube root of x,
    then a better approximation is given by the value

    (x/y^2 + 2y) / 3
    Use this formula to implement a cube-root procedure 
    analogous to the square-root procedure. 
'''

EXP = 0.001

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return (x/pow(guess, 2) + 2*guess) / 3

def good_enough(guess, new_guess):
    # return abs(x - pow(guess, 2)) < EXP
    return (abs(guess - new_guess)/guess) < 0.01

def cuberoot_iter(guess, x):
    if good_enough(guess, improve(guess, x)):
        return improve(guess, x)
    else:
        return cuberoot_iter(improve(guess, x), x)

def cuberoot(x):
    return cuberoot_iter(1.0, x)

def main():
    x = float(input())
    print(x)
    print(cuberoot(x))

if __name__ == "__main__":
    main()