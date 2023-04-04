#!/usr/bin/env python3

'''
Exercise 1.17:
    Now suppose we include, together with addition, opera-
tions double, which doubles an integer, and halve, which
divides an (even) integer by 2. Using these, design a mul-
tiplication procedure analogous to fast-expt that uses a
logarithmic number of steps.

'''

def double(x):
    return x + x

def halve(x):
    return x // 2

def is_even(x):
    return double(halve(x)) == x

def mul(a, b):
    if b == 0:
        return 0
    elif is_even(b):
        return double(mul(a, halve(b)))
    else:
        return a + mul(a, b-1)        

def main():
    a = int(input())
    b = int(input())
    res = mul(a, b)
    print(res)
    # print(double(a))
    # print(halve(b))
    
if __name__ == "__main__":
    main()