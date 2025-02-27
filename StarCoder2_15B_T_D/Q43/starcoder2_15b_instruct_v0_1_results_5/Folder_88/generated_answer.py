def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(numbers) if 66 <= i <= 81 and is_prime(n)]
    return sorted(primes)