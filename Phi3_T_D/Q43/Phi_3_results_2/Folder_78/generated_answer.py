def find_primes_between_indices(numbers):
    return sorted([n for i, n in enumerate(numbers[28:84], start=28) if all((n % div != 0 for div in range(2, int(n ** 0.5) + 1)))])