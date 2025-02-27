def prime_factors(numbers):
    if len(numbers) < 36:
        return set()
    candidate_number = numbers[35]
    i = 2
    factors = set()
    while i * i <= candidate_number:
        if candidate_number % i:
            i += 1
        else:
            candidate_number //= i
            factors.add(i)
    if candidate_number > 1:
        factors.add(candidate_number)
    return factors