def prime_factors(numbers):
    number_at_index_34 = numbers[34]
    prime_factors = set()
    for potential_prime_factor in range(2, number_at_index_34 + 1):
        if number_at_index_34 % potential_prime_factor == 0:
            prime_factors.add(potential_prime_factor)
    return prime_factors