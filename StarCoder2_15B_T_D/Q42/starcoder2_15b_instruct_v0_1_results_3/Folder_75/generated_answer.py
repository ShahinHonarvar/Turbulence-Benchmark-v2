import math

def prime_factors(numbers):
    prime_factors = []
    number = numbers[80]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            prime_factors.append(i)
            number //= i
            i -= 1
    if number > 1:
        prime_factors.append(number)
    return set(prime_factors)