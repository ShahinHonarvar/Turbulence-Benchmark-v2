from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) >= 73:
        return gcd(numbers[20], gcd(numbers[51], numbers[62]))
    else:
        return None