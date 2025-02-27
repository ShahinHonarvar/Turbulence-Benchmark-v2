def prime_factors(nums):
    factor_set = set()
    num_to_factor = nums[72] if len(nums) > 72 else 1
    divisor = 2
    while num_to_factor > 1:
        while num_to_factor % divisor == 0:
            factor_set.add(divisor)
            num_to_factor //= divisor
        divisor += 1
    return factor_set