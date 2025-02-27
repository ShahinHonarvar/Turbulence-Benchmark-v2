from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[1], numbers[2], numbers[7])
    return gcd(gcd(a, b), c)