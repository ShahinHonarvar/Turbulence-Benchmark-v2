def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        if n not in primes:
            return False
        if n < 10:
            return True
        return is_left_truncatable(int(str(n)[1:]), primes)
    x = numbers[33]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatables = [p for p in primes if is_left_truncatable(p, primes)]
    return truncatables