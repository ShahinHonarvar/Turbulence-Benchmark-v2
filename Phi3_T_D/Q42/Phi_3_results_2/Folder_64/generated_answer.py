def prime_factors(nums):
    if len(nums) < 2:
        return set()
    num = nums[1]
    factors = set()
    divisor = 2
    while divisor ** 2 <= num:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        factors.add(num)
    return factors