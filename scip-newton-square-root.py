#!/usr/bin/env python3

EXP = 0.001

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, x/guess)

def good_enough(guess, x):
    return abs(x - pow(guess, 2)) < EXP

def sqrt_iter(guess, x):
    if good_enough(guess, improve(guess, x)):
        return improve(guess, x)
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)

def main():
    x = float(input())
    print(x)
    print(sqrt(x))

if __name__ == "__main__":
    main()