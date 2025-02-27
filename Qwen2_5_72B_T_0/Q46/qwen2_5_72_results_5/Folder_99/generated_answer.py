from math import gcd

def gcf_three_nums(numbers):
    a = numbers[912]
    b = numbers[170]
    c = numbers[500]
    return gcd(gcd(a, b), c)