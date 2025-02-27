def find_primes_between_indices(lst):
    primes = [x for x in lst[12:30] if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1))) and x > 1]
    return sorted(primes, reverse=True)