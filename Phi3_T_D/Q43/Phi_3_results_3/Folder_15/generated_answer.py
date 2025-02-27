def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2 or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return True
    primes = sorted([n for n in numbers[6:8] if is_prime(n)], reverse=True)
    return primes