def all_left_truncatable_prime(x):
    number = x[792]

    def is_left_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(1, 10):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    for i in range(10, number):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)