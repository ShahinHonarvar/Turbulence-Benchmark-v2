from math import gcd

def gcf_two_nums(numbers):
    return gcd(numbers[83], numbers[14]) if len(numbers) > 14 and 83 < len(numbers) else None