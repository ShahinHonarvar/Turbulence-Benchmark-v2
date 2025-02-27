def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable():
        primes = {str(prime) for prime in range(2, x)}
        for prime_str in str(prime):
            new_prime_str = prime_str[1:]
            if new_prime_str not in primes:
                return False
        return True
    x = numbers[88]
    left_truncatable_primes = []
    for prime in range(2, x):
        if is_left_truncatable(str(prime)):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes