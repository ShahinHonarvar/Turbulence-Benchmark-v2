def all_right_truncatable_prime(numbers):
    x = numbers[64]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primes):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if is_prime(num):
            primes.append(num)
    right_truncatables = [p for p in primes if is_right_truncatable(p, primes)]
    return sorted(right_truncatables, reverse=True)