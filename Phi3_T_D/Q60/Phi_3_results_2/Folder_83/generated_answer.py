def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if is_prime(int(str_n[i:])) is False or is_prime(int(str_n[:-i])) is False:
                return False
        return True

    def primes_below(n):
        return [x for x in range(2, n + 1) if is_prime(x)]
    x = numbers[24]
    all_primes_below_x = primes_below(x)
    trunc_primes = [p for p in all_primes_below_x if is_truncatable_prime(p, all_primes_below_x)]
    return trunc_primes