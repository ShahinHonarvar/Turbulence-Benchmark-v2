import math

def gcf_three_nums(numbers):
    try:
        index_90, index_54, index_96 = (numbers[90], numbers[54], numbers[96])
        return math.gcd(math.gcd(index_90, index_54), index_96)
    except IndexError as e:
        raise IndexError('List does not have enough elements') from e