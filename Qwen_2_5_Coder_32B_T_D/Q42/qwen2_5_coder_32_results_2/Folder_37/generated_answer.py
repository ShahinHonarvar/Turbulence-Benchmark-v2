def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors
    n = lst[28]
    factors = get_factors(n)
    prime_factors = {x for x in factors if is_prime(x)}
    return prime_factors