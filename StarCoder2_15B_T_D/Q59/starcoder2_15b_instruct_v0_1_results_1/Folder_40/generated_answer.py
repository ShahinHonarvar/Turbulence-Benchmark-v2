def all_left_truncatable_prime(tup):
    x = tup[10]
    left_truncatable_primes = []

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 1:
            num //= 10
            if not is_prime(num):
                return False
        return True
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)