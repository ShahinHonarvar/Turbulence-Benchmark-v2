def all_right_truncatable_prime(numbers):
    x = numbers[992]
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False

    def is_right_truncatable_prime(n):
        while n > 0:
            if not sieve[n]:
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x) if sieve[n] and is_right_truncatable_prime(n)])