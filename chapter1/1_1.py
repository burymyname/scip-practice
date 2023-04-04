#!/usr/bin/env python3

'''
Exercise 1.1: 
    Below is a sequence of expressions. What is the result 
    printed by the interpreter in response to each expression? 
    Assume that the sequence is to be evaluated in the order 
    in which it is presented.
'''

def main():
    print(10)
    print(5+3+4)
    print(9-1)
    print(6/2)
    print((2*4)+(4-6))
    a = 3
    print(a)
    b = a + 1
    print(a+b+a*b)
    print(a==b)

    if b > a and b < a*b:
        print(b)
    else:
        print(a)

    if a == 4:
        print(6)
    elif b == 4:
        print(6+7+a)
    else:
        print(25)

    print(2 + (b if b > a else a))
    
    if a > b :
        n = a
    elif a < b:
        n = b
    else:
        n = -1
    print(n * (a + 1))

if __name__ == "__main__":
    main()