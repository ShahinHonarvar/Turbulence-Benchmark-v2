def prime_factors(numbers):
    return set((p for i in numbers for p in prime_factors_of(numbers[i])))

def prime_factors_of(n):
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