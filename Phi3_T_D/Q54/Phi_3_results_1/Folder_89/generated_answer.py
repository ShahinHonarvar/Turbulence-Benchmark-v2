def all_right_truncatable_prime(tpl):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if is_prime(n) and n not in primes:
            return [n] + sum((is_right_truncatable_prime(n // 10, primes + [n]) for n in [n]), [])
        return []
    x = tpl[97]
    primes = [2]
    right_truncatable_primes = []
    for prime in is_right_truncatable_prime(x, primes):
        primes.append(prime)
        right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)