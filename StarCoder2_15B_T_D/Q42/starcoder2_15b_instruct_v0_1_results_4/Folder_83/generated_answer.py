def prime_factors(numbers):
    return set(prime_factors_helper(numbers[95]))

def prime_factors_helper(n):
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors