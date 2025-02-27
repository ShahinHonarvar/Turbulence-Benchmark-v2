import math

def prime_factors(numbers):
    number = numbers[3]
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number //= 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
    if number > 2:
        prime_factors.append(number)
    return set(prime_factors)