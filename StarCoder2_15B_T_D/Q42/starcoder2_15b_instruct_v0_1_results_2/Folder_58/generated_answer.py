import math

def prime_factors(lst):
    number = lst[714]
    prime_factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
    if number > 1:
        prime_factors.append(number)
    return set(prime_factors)