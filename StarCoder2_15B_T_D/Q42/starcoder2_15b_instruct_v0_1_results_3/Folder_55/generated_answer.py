def prime_factors(nums):
    return set(prime_factorization(nums[21]))

def prime_factorization(num):
    factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors