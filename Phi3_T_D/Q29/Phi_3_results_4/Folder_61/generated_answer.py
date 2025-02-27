import math

def gcf_two_nums(numbers):
    if len(numbers) < 9:
        raise ValueError('List must contain at least 9 elements')
    return math.gcd(numbers[8], numbers[3])