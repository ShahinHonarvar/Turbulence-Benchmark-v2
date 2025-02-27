def prime_factors(lst):

    def prime_factors_number(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    if len(lst) > 4:
        return prime_factors_number(lst[4])
    else:
        raise ValueError('The list does not contain enough elements.')