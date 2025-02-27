def prime_factors(nums):
    if len(nums) < 64:
        raise IndexError('Index 63 is out of range')
    num = nums[63]
    factors = set()
    factor = 2
    while num > 1:
        while num % factor == 0:
            factors.add(factor)
            num //= factor
        factor += 1
    return factors