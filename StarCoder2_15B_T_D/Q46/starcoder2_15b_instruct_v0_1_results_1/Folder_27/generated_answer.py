from math import gcd   # Import the gcd function from the math module

def gcf_three_nums(numbers):
    return gcd(numbers[76], gcd(numbers[64], numbers[28]))