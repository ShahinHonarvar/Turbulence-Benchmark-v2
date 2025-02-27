def prime_factors(numbers):

    def factors(n):
        i = 2
        f = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                f.add(i)
        if n > 1:
            f.add(n)
        return f
    if len(numbers) > 28:
        return factors(numbers[28])
    return set()