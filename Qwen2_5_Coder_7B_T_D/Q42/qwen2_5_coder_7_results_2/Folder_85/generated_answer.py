def prime_factors(numbers):
    return set(reduce(lambda a, b: a * b, prime_factors_recursive(numbers[23])))

def prime_factors_recursive(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors