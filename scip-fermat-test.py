#!/usr/bin/env python3

import random

def is_even(x):
    return x % 2 == 0

def square(x):
    return x * x

def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif is_even(exp):
        return square(expmod(base, exp/2, m)) % m
    else:
        return base * (expmod(base, exp-1, m)) % m

def try_it(a, n):
    return expmod(a, n, n) == a

def fermat_test(n):
    return try_it(random.randint(0, n-1), n)

def fast_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times-1)
    else:
        return False

def main():
    print(expmod(2, 10, 5))
    print(fast_prime(5, 10))
    # print(is_even(1))
    # print(is_even(2))


if __name__ == "__main__":
    main()