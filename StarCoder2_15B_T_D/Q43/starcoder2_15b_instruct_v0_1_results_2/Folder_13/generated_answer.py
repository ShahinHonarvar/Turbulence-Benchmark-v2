def find_primes_between_indices(numbers):
    """
    Finds all prime numbers in a list of integers within the specified range.
    """

    def is_prime(n):
        """
        Checks if a number is prime.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(numbers) if 415 <= i <= 647 and is_prime(n)]
    primes.sort()
    return primes