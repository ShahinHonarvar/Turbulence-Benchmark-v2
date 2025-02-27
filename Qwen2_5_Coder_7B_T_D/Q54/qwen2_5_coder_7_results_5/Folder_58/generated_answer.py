def all_right_truncatable_prime(t):
    x = t[975]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for prime in primes:
        for digit in range(1, 10):
            new_prime = prime * 10 + digit
            if new_prime < x and is_prime(new_prime):
                right_truncatable_primes.append(new_prime)
                right_truncatable_primes.extend([int(str(new_prime)[:i]) for i in range(1, len(str(new_prime)))])
    return sorted(set(right_truncatable_primes), reverse=True)