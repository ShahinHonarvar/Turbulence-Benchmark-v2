def all_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    x = numbers[49]

    def is_prime(n):
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p = p // 10
        return True
    right_truncs = [p for p in range(2, x) if truncatable(p)]
    return sorted(right_truncs, reverse=True)