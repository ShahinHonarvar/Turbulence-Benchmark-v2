import math

def gcf_three_nums(numbers):
    try:
        return math.gcd(numbers[20], math.gcd(numbers[35], numbers[74]))
    except IndexError:
        raise ValueError('List index out of range')