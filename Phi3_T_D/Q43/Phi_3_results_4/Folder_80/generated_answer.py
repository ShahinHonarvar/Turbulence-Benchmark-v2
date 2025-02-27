def find_primes_between_indices(lst):
    primes = [x for x in lst[12:30] if all((x % d for d in range(2, int(x ** 0.5) + 1)))]
    primes.sort(reverse=True)
    return primes