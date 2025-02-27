from math import gcd

def gcf_three_nums(numbers):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[558]
    b = numbers[110]
    c = numbers[628]
    return find_gcf(find_gcf(a, b), c)