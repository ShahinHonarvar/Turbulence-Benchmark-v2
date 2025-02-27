def find_primes_between_indices(lst):
    return sorted([x for i, x in enumerate(lst) if i >= 25 and i <= 72 and is_prime(x)])

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True