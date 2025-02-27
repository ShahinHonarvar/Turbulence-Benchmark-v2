def all_left_truncatable_prime(numbers):
    x = numbers[370]
    primes_cache = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        p = 2
        while p * p <= n:
            if n % p == 0:
                return False
            p += 1
        return True

    def is_left_truncatable(n):
        if n < 10:
            return True
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)