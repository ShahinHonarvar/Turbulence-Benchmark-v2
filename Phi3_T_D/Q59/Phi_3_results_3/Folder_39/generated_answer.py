def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[30]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable = [p for p in primes if is_left_truncatable(p, primes)]
    return sorted(left_truncatable, reverse=True)