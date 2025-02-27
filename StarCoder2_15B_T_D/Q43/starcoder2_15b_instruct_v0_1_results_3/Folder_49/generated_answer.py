def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = []
    for i, n in enumerate(numbers):
        if is_prime(n) and 22 <= i <= 50:
            primes.append(n)
    return sorted(primes, reverse=True)