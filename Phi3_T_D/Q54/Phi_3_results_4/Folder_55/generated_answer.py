def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(prime, digits):
        if not prime.startswith(digits):
            return False
        while len(prime) > 0:
            if not is_prime(int(prime)):
                return False
            prime = prime[:-1]
        return True
    x = numbers[73]
    right_truncatable_primes = []
    for prime in range(2, x):
        if is_prime(prime) and is_right_truncatable_prime(str(prime), ''):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)