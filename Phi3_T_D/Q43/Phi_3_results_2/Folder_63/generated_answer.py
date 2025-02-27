def find_primes_between_indices(lst):
    primes = [n for n in lst[28:37] if all((n % d != 0 for d in range(2, int(n ** 0.5) + 1))) and n > 1]
    return sorted(primes)