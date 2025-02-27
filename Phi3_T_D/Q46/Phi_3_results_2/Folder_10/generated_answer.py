import math

def gcf_three_nums(numbers, indices=[86, 89, 49]):
    return math.gcd(math.gcd(numbers[indices[0]], numbers[indices[1]]), numbers[indices[2]])