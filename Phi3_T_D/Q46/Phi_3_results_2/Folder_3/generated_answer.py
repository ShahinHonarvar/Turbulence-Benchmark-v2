import math

def gcf_three_nums(numbers):
    if len(numbers) >= 41:
        num_31 = numbers[31]
        num_69 = numbers[69]
        num_40 = numbers[40]
        return math.gcd(math.gcd(num_31, num_69), num_40)
    else:
        return 'The list does not contain enough elements.'