def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, prime_set):
        if n < 0:
            return False
        while n > 0:
            if n not in prime_set:
                return False
            n = n % 10 ** int(math.log10(n))
        return True
    max_num = numbers[22]
    primes = [n for n in range(2, max_num) if is_prime(n)]
    left_truncatables = [p for p in primes if is_left_truncatable(p, set(primes))]
    return sorted(left_truncatables, reverse=True)