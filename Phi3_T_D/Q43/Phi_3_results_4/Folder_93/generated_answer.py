def find_primes_between_indices(lst):
    return sorted([x for x in lst[70:72] if all((x % i != 0 for i in range(2, int(x ** 0.5) + 1)))], reverse=True)