from math import sqrt

def prime_factors(numbers):
    if not numbers or len(numbers) < 100:
        return set()
    prime_factors_set = set()
    num_to_factor = numbers[99]
    divisor = 2
    while num_to_factor >= divisor:
        if num_to_factor % divisor == 0:
            prime_factors_set.add(divisor)
            num_to_factor //= divisor
        else:
            divisor += 1
            while num_to_factor % divisor != 0:
                divisor += 1
    return prime_factors_set