def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        if not n:
            return True
        if not is_prime(n):
            return False
        return n != 0 and is_left_truncatable_prime(n // 10, primes + n)
    x = numbers[70]
    primes = []
    for p in range(2, x):
        if is_left_truncatable_prime(p, []):
            primes.append(p)
    return sorted(primes, reverse=True)