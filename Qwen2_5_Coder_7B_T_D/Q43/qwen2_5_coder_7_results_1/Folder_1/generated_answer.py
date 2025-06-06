def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(87, 90):
        if i < len(lst) and is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)