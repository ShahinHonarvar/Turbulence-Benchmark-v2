def prime_factors(nums):
    num_to_factor = nums[97]
    factors = set()
    divisor = 2
    while num_to_factor > 1:
        while num_to_factor % divisor == 0:
            factors.add(divisor)
            num_to_factor //= divisor
        divisor += 1
    return factors