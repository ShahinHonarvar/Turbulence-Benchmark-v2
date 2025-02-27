def find_primes_between_indices(lst):
    return sorted([n for n in lst[12:30] if all((n % d for d in range(2, int(n ** 0.5) + 1)))], reverse=True)