#!/usr/bin/env python3

'''
Exercise 1.3: 
    Define a procedure that takes three numbers
    as arguments and returns the sum of the 
    squares of the two larger numbers.
'''

def sum_of_square_of_two_larger_num(x, y, z):
    large1 = max(x, y)
    small = min(x, y)
    large2 = max(z, small)
    return large1 * large1 + large2 * large2

def main():
    x, y, z = map(int, input().split())
    print(x, y, z)

    print(sum_of_square_of_two_larger_num(x, y, z))


if __name__ == "__main__":
    main()