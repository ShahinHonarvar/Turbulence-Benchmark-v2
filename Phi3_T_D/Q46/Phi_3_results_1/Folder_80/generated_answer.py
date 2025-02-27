import math

def gcf_three_nums(numbers):
    if len(numbers) < 45:
        raise ValueError('List must have at least 45 elements')
    return math.gcd(numbers[13], math.gcd(numbers[76], numbers[44]))