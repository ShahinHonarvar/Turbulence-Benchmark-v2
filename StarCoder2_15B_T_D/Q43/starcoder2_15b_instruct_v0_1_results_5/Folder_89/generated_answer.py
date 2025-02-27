def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(l):
    primes = []
    for i, n in enumerate(l):
        if is_prime(n) and 69 <= i <= 84:
            primes.append(n)
    return sorted(primes, reverse=True)