def all_right_truncatable_prime(t):
    x = t[26]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes