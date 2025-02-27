def prime_factors(numbers):
    number_at_index_80 = numbers[80]
    prime_factors = []
    candidate_factor = 2
    while candidate_factor <= number_at_index_80:
        if number_at_index_80 % candidate_factor == 0:
            prime_factors.append(candidate_factor)
            number_at_index_80 //= candidate_factor
        else:
            candidate_factor += 1
    return set(prime_factors)