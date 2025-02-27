from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[24], numbers[25], numbers[80])
    return gcd(gcd(a, b), c)