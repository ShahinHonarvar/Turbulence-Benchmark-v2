def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, primes):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
                return False
        return True
    primes = [i for i in range(2, numbers[65] + 1) if is_prime(i)]
    left_right_primes = [p for p in primes if is_truncatable(p, primes)]
    return sorted(left_right_primes, reverse=True)