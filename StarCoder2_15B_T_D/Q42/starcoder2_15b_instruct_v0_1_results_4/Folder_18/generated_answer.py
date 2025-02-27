def prime_factors(nums):
    n = nums[312]
    return set((n for i in range(2, n + 1) for n in divmod(n, i) if n))