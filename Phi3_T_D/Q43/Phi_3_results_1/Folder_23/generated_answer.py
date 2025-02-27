def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index, end_index = (20, 48)
    primes = [n for i, n in enumerate(lst) if is_prime(n) and start_index <= i <= end_index]
    return sorted(primes, reverse=True)