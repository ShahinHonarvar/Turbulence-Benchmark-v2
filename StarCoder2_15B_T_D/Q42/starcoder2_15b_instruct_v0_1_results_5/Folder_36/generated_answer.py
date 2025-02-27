import math

def prime_factors(numbers):
    number = numbers[990]
    sqrt_number = int(math.sqrt(number))
    prime_factors = set()
    for i in range(2, sqrt_number + 1):
        while number % i == 0:
            prime_factors.add(i)
            number //= i
    if number > 1:
        prime_factors.add(number)
    return prime_factors