import math

def gcf_three_nums(numbers):
    try:
        return math.gcd(numbers[86], math.gcd(numbers[89], numbers[49]))
    except IndexError:
        raise IndexError('List indices are out of range.')