def find_primes_between_indices(lst):
    return sorted((x for x in lst[10:67] if x > 1 and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))))