def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(k, primes):
        while k > 0:
            if not is_prime(k):
                return False
            k = k // 10
        return True
    primes = [2, 3, 5, 7]
    for i in range(10, numbers[29]):
        if is_right_truncatable(i, primes):
            primes.append(i)
    right_truncatable_primes = sorted({p for p in primes if len(str(p)) >= 3})
    return right_truncatable_primes