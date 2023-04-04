#!/usr/bin/env python3

'''
Exercise 1.2: 
    Translate the following expression into prefix form: 
        (5+4+(2-(3-(6+4/5))))/(3*(6-2)*(2-7))

    (/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5) ) ) ) ) (* 3 (- 6 2) (- 2 7))
'''

def inorder2prefix(string):
    pass


def main():
    expr = input()
    inorder2prefix(expr)

if __name__ == "__main__":
    main()