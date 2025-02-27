def prime_factors(numbers):
    factors = set()
    if 45 < len(numbers):
        n = numbers[45]
        divisor = 2
        while n >= divisor * divisor:
            if n % divisor:
                divisor += 1
            else:
                n //= divisor
                factors.add(divisor)
        factors.add(n)
    return factors