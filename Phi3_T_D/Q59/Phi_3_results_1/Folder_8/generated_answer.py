def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(primes_set, n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    x = numbers[41]
    n = 2
    truncatables = []
    while n < x:
        if is_left_truncatable({n}, n):
            truncatables.append(n)
        n += 1
    return sorted(truncatables, reverse=True)