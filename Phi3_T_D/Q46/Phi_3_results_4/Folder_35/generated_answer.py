from math import gcd

def gcf_three_nums(numbers):
    index_742 = 742 % len(numbers)
    index_888 = 888 % len(numbers)
    index_629 = 629 % len(numbers)
    return gcd(numbers[index_742], gcd(numbers[index_888], numbers[index_629]))