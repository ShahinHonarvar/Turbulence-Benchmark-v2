from math import gcd

def gcf_three_nums(numbers):
    a = numbers[818]
    b = numbers[606]
    c = numbers[873]
    temp1 = gcd(a, b)
    result = gcd(temp1, c)
    return result