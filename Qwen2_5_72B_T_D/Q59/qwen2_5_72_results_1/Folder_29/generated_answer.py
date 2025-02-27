def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[55]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_left_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)