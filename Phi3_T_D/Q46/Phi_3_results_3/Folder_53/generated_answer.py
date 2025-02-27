from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) > max(66, 56, 92):
        return gcd(numbers[66], gcd(numbers[56], numbers[92]))
    else:
        raise IndexError('List too short.')