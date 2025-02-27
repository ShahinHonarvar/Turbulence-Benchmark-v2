def prime_factors(numbers):
    n = numbers[90]
    factors = set()
    divisor = 2
    while divisor ** 2 <= n:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.add(n)
    return factors