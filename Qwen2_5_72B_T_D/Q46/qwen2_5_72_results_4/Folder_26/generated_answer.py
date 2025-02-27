from math import gcd

def gcf_three_nums(numbers):
    x, y, z = (numbers[15], numbers[51], numbers[76])
    return gcd(gcd(x, y), z)