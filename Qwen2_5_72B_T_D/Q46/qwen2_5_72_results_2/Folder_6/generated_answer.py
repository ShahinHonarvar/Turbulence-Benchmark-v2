from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[93], numbers[94], numbers[57])
    return gcd(gcd(a, b), c)