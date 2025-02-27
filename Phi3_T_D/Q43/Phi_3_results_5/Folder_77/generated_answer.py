def find_primes_between_indices(lst):
    primes_in_range = [x for x in lst[287:929] if x > 1 and all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))]
    return sorted(primes_in_range)