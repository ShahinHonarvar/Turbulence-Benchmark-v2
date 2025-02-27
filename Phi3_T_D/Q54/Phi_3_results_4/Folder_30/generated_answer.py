def all_right_truncatable_prime(numbers):
    x = numbers[37]
    right_truncatable_primes = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n = n // 10
            if not is_prime(n):
                return False
        return True
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.add(i)
    return sorted(list(right_truncatable_primes), reverse=True)