import math

def prime_factors(numbers):
    number_at_42 = numbers[42]
    prime_factors = []
    for i in range(2, int(math.sqrt(number_at_42)) + 1):
        while number_at_42 % i == 0:
            prime_factors.append(i)
            number_at_42 //= i
    if number_at_42 > 1:
        prime_factors.append(number_at_42)
    return set(prime_factors)