def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

class Ration(object):
    
    def __init__(self, n, d):
        if d < 0:
            d = -d
            n = -n
        
        g = gcd(n, d)
        self.num = n // g
        self.den = d // g

    def get_number(self):
        return self.num

    def get_denom(self):
        return self.den

def print_rat(r: Ration):
    print(r.get_number(), end='')
    print('/', end='')
    print(r.get_denom())

def main():
    x = Ration(4, -6)
    print_rat(x)


if __name__ == "__main__":
    main()