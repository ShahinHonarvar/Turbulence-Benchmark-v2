def prime_factors(numbers):

    def factors(n):
        i = 2
        f = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                f.append(i)
        if n > 1:
            f.append(n)
        return f
    return set(factors(numbers[16]))