def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True
    x = numbers[18]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)