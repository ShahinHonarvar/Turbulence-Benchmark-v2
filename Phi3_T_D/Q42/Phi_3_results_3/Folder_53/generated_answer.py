def prime_factors(nums):
    if 73 < len(nums) and nums[73] > 1:
        factors = set()
        d = 2
        while d * d <= nums[73]:
            while nums[73] % d == 0:
                factors.add(d)
                nums[73] //= d
            d += 1
        if nums[73] > 1:
            factors.add(nums[73])
        return factors
    return 'No value at index 73'