def prime_factors(numbers):
    n = numbers[990]
    prime_factors = []
    i = 2
    while i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 1
    return set(prime_factors)