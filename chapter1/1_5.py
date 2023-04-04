#!/usr/bin/env python3
'''
Exercise 1.5: 
    Ben Bitdiddle has invented a test to determine
    whether the interpreter he is faced with is using 
    applicative-order evaluation or normal-order evaluation. 
    He defines the following two procedures:

        (define (p) (p))
        (define (test x y)
        (if (= x 0) 0 y))

    Then he evaluates the expression
        (test 0 (p))
    
Answer:
    Maybe the applicative-order evaluation will result in
    unlimited recursive.
'''

def main():
    pass

if __name__ == "__main__":
    main()