from math import gcd

def gcf_three_nums(numbers):
    a = numbers[341]
    b = numbers[238]
    c = numbers[374]
    return gcd(gcd(a, b), c)