def prime_factors(nums):
    return set(prime_factors_of(nums[80]))

def prime_factors_of(n):
    factors = []
    divisor = 2
    while n >= divisor * divisor:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors