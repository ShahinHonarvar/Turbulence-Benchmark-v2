from math import sqrt

def prime_factors(numbers):
    number = numbers[28]
    for i in range(2, int(sqrt(number)) + 1):
        while number % i == 0:
            number //= i
    return number