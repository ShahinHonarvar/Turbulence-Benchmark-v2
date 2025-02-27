def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start, end = (61, 79)
    primes = [n for n in lst[start:end + 1] if is_prime(n)]
    return sorted(primes)