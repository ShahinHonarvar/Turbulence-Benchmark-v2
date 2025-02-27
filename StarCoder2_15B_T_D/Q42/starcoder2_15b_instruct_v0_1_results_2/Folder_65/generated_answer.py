def prime_factors(nums):
    num = nums[35]
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return set(factors)