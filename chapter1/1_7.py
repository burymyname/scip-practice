#!/usr/bin/env python3

'''
Exercise 1.7: 
    The good-enough? test used in computing square roots 
    will not be very effective for finding the square
    roots of very small numbers. Also, in real computers, 
    arithmetic operations are almost always performed with 
    limited precision. This makes our test inadequate for 
    very large numbers. Explain these statements, 
    with examples showing how the test fails for small and 
    large numbers. An alternative strategy for implementing 
    good-enough? is to watch how guess changes from one iteration 
    to the next and to stop when the change is a very small 
    fraction of the guess. Design a square-root procedure that 
    uses this kind of end test. Does this work beer for small 
    and large numbers?

Answer:
    Use the ratio of difference between the new guess and 
    old guess to the old guess
'''

EXP = 0.001

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, x/guess)

def good_enough(guess, new_guess):
    # return abs(x - pow(guess, 2)) < EXP
    return (abs(guess - new_guess)/guess) < 0.01

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