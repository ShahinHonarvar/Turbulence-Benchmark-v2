import math

def gcf_three_nums(numbers):
    try:
        indices = [404, 834, 517]
        three_nums = [numbers[idx - 1] for idx in indices]
        return math.gcd(three_nums[0], math.gcd(three_nums[1], three_nums[2]))
    except IndexError:
        return 'Indices out of range for the given list'