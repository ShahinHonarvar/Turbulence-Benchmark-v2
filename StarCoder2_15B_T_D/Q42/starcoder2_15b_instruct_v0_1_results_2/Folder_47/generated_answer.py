def prime_factors(nums):
    num = nums[34]
    factors = set()
    factor = 2
    while num > 1:
        if num % factor == 0:
            factors.add(factor)
            num //= factor
        else:
            factor += 1
    return factors