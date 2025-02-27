from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[76], numbers[35], numbers[74])
    return gcd(gcd(a, b), c)