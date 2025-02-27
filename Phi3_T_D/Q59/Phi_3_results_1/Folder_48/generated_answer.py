def all_left_truncatable_prime(tpl):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tpl[835]
    primes = [p for p in range(2, x) if is_prime(p)]
    truncatable_primes = [str(p) for p in primes if all((is_prime(int(p[i:])) for i in range(len(str(p))))) and '0' not in str(p)]
    return truncatable_primes