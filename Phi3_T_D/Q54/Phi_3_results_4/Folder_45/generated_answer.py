def all_right_truncatable_prime(numbers_tuple):

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
    limit = numbers_tuple[61]
    primes = set()
    for num in range(2, limit):
        if is_prime(num) and is_right_truncatable(num, primes):
            primes.add(num)
    return sorted(list(primes))