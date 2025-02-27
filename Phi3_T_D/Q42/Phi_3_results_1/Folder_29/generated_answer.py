def prime_factors(numbers):

    def factors(n, i=2):
        if n <= 1:
            return
        if n % i == 0:
            yield i
            while n % i == 0:
                n //= i
        if n == 1:
            return
        yield from factors(n)
    num = numbers[19]
    return set(factors(num))