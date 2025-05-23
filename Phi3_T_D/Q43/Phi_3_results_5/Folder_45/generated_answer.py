def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = [n for i, n in enumerate(numbers) if is_prime(n) and 23 <= i <= 39]
    prime_numbers.sort()
    return prime_numbers