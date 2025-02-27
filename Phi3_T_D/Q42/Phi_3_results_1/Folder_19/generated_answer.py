def prime_factors(lst):

    def prime_factorization(n):
        factors = []
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            factors.append(n)
        return set(factors)
    if len(lst) > 13:
        return prime_factorization(lst[13])
    else:
        return set()