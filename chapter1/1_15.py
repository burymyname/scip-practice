#!/usr/bin/env python3

'''
The sine of an angle (specified in radians)
can be computed by making use of the approximation sin x = x

'''
COUNTER=0

def cube(x):
    return x * x * x

def p(x):
    global COUNTER
    COUNTER += 1
    return 3 * x - 4 * cube(x)

def sin(angle):
    if abs(angle) > 0.1:
        return p(sin(angle/3.0))
    else:
        return angle

def main():
    res = sin(12.15)
    print(res)
    print(COUNTER)

if __name__ == "__main__":
    main()