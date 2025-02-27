def prime_factors(lst):

    def prime_gen(n):
        yield 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                yield i
                while n % i == 0:
                    n //= i
        if n > 2:
            yield n
    try:
        factor_set = set(prime_gen(lst[66]))
    except IndexError:
        raise ValueError('The list has fewer than 67 elements, cannot find the 66th element.')
    return factor_set