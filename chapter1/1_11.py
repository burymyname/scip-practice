#!/usr/bin/env python3

'''
Exercise 1.11: 
    A function f is defined by the rule that
    f(n) = n if n < 3
         = f(n-1) + 2f(n-2) + 3f(n-3) if n >= 3
    Write a procedure that computes f by means of a recursive
    process. Write a procedure that computes f by means of an
    iterative process
'''

def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2*f(n-2) + 3*f(n-3)

def fi(n):
    if n < 3:
        return n
    else:
        end = n - 3 + 1
        i0 = 0
        i1 = 1
        i2 = 2
        i = 0
        for i in range(end):
            i = 3*i0 + 2*i1 + i2
            i0 = i1
            i1 = i2
            i2 = i
        return i
        

def main():
    n = int(input())
    print(f(n))
    print(fi(n))

if __name__ == "__main__":
    main()