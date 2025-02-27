def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(numbers) if is_prime(n) and 13 <= i <= 63]
    primes.sort()
    return primes