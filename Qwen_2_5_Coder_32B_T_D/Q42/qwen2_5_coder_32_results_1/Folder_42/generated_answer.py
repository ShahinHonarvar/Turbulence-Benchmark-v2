def prime_factors(numbers):

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n
    return set(factors(numbers[276]))