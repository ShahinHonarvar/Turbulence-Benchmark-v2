def prime_factors(lst):
    n = lst[69]
    factors = set()
    divisor = 2
    while n >= divisor:
        if n % divisor == 0 and all((divisor % i != 0 for i in range(2, int(divisor ** 0.5) + 1))):
            factors.add(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors