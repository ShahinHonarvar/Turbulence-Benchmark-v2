import math

def gcf_two_nums(numbers):
    if len(numbers) > 31 and len(numbers) > 49:
        return math.gcd(numbers[49], numbers[31])
    else:
        raise ValueError('List must contain at least 50 elements.')