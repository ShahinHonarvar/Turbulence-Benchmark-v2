def find_primes_between_indices(lst):
    prime_indices = range(430, 806)
    primes = [lst[i] for i in prime_indices if is_prime(lst[i])]
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True