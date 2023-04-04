#!/usr/bin/env python3

'''
Counting change
The number of ways to change amount a using n kinds of coin =
    - The number of ways to change amount a using all but the first kind of coin
        +
    - The number of ways to change amount a - d using all n kinds of coin, where d is the denomination of the first kind of coin
'''

def first_denomination(kind_of_coin):
    if kind_of_coin == 1:
        return 1
    elif kind_of_coin == 2:
        return 5
    elif kind_of_coin == 3:
        return 10
    elif kind_of_coin == 4:
        return 25
    elif kind_of_coin == 5:
        return 50


def cc(amount, kind_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kind_of_coins == 0:
        return 0
    else:
        return cc(amount, kind_of_coins-1) + cc(amount-first_denomination(kind_of_coins), kind_of_coins)

def count_change(amount):
    return cc(amount, 5)

def main():
    res = count_change(100)
    print(res)

if __name__ == "__main__":
    main()