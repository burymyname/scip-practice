#!/usr/bin/env python3

def square(n):
    return n * n

def divides(a, b):
    return a % b == 0

def find_divisor(n, test_divisor):
    if square(test_divisor) > n:
        return n
    elif divides(n, test_divisor):
        return test_divisor
    else:
        return find_divisor(n, test_divisor+1)

def smallest_divisor(n):
    return find_divisor(n, 2)

def main():
    n = int(input())
    res = smallest_divisor(n)
    print(res)

if __name__ == "__main__":
    main()