from math import gcd

def gcf_three_nums(numbers):
    if len(numbers) < max(41, 69, 28):
        return None
    num_41 = numbers[41]
    num_69 = numbers[69]
    num_28 = numbers[28]
    return gcd(gcd(num_41, num_69), num_28)