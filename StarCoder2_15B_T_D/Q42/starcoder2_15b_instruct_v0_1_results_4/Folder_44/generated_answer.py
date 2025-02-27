def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    number_at_index_828 = numbers[828]
    factors = []
    for i in range(2, number_at_index_828 + 1):
        if number_at_index_828 % i == 0 and is_prime(i):
            factors.append(i)
    return set(factors)