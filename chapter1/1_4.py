#!/usr/bin/env python3

'''
Exercise 1.4: 
    Observe that our model of evaluation allows
    for combinations whose operators are compound 
    expressions. Use this observation to describe 
    the behavior of the following procedure
'''

def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b

def main():
    a, b = map(int, input().split())
    print(a_plus_abs_b(a, b))

if __name__ == "__main__":
    main()