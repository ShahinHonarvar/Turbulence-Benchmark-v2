def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, prime_cache={2, 3, 5, 7}):
        while n > 0:
            if n not in prime_cache:
                return False
            n = n % (10 ** len(str(n)) // 10)
        return True
    return sorted(filter(lambda p: is_left_truncatable_prime(p, prime_cache={2, 3, 5, 7}), range(2, x)), reverse=True)