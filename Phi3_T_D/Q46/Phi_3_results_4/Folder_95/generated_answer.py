from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < max(87, 20, 36):
        raise IndexError('One of the specified indices is out of range.')
    result = gcd(numbers[87], gcd(numbers[20], numbers[36]))
    return result