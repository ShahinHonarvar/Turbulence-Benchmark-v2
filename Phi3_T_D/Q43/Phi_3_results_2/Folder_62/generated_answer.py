def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start, end = (29, 97)
    primes = [x for i, x in enumerate(lst) if is_prime(x) and start <= i <= end]
    return sorted(primes, reverse=True)