from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < 3 or len(numbers) < 74 or len(numbers) < 60 or (len(numbers) < 28):
        raise ValueError('List must have at least 74 elements')
    return gcd(numbers[73], gcd(numbers[59], numbers[27]))