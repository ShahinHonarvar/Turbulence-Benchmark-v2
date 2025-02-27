from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[96], numbers[53], numbers[35])
    return gcd(gcd(a, b), c)