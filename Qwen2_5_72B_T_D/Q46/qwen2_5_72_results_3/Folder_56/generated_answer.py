from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[59], numbers[93], numbers[84])
    return gcd(gcd(a, b), c)