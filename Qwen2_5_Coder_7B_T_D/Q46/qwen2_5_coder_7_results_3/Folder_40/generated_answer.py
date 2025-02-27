from math import gcd

def gcf_three_nums(numbers):
    return gcd(gcd(numbers[1], numbers[6]), numbers[8])