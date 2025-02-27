from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 77 or any((i not in range(16, 77) for i in [15, 51, 76])):
        raise ValueError('List must have at least 77 elements and indices 15, 51, and 76 must exist.')
    return gcd(gcd(numbers[15], numbers[51]), numbers[76])