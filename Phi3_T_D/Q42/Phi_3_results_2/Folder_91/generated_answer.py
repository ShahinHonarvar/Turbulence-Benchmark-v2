def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def collect_prime_factors(n):
        factors = set()
        div = 2
        while div * div <= n:
            if n % div:
                div += 1
            else:
                n //= div
                if is_prime(div):
                    factors.add(div)
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    return collect_prime_factors(lst[6]) if len(lst) > 6 else set()