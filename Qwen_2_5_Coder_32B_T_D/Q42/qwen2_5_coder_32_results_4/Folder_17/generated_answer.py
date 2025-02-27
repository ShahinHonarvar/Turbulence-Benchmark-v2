def prime_factors(numbers):

    def factors(n):
        i, f = (2, set())
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                f.add(i)
        if n > 1:
            f.add(n)
        return f
    return factors(numbers[632])