def prime_factors(numbers):

    def factors(n):
        result = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                result.add(d)
                n //= d
            d += 1
        if n > 1:
            result.add(n)
        return result
    return factors(numbers[0])