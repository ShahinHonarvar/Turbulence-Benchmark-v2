def prime_factors(lst):

    def get_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    try:
        number = lst[733]
        return get_prime_factors(number)
    except IndexError:
        return 'Index out of range'