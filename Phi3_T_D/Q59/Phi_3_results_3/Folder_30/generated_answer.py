def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        if n == 0:
            return True
        if not is_prime(n):
            return False
        return is_left_truncatable_prime(n // 10, primes)
    x = numbers[37]
    primes = [2]
    truncatable_primes = []
    for i in range(3, x, 2):
        if is_left_truncatable_prime(i, primes):
            primes.append(i)
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)