from math import gcd

def gcf_three_nums(numbers):
    x = gcd(numbers[341], numbers[238])
    y = gcd(x, numbers[374])
    return y