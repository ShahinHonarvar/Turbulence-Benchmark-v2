def find_primes_between_indices(lst):
    primes = [x for x in lst[33:36] if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))]
    return sorted(primes)