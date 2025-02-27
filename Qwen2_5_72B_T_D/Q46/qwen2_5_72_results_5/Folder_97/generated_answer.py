from math import gcd

def gcf_three_nums(numbers):
    a = numbers[944]
    b = numbers[814]
    c = numbers[865]
    return gcd(gcd(a, b), c)