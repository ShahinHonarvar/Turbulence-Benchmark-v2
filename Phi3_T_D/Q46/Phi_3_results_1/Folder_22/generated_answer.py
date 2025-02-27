from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 3:
        return None
    return gcd(numbers[27], gcd(numbers[85], numbers[51]))