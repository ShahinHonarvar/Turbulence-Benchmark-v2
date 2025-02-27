from math import gcd

def gcf_three_nums(numbers):
    a = numbers[876]
    b = numbers[203]
    c = numbers[100]
    return gcd(gcd(a, b), c)