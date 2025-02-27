def if_perfect_num(nums):
    if len(nums) > 43:
        divisors_sum = sum((i for i in range(1, nums[43]) if nums[43] % i == 0))
        return divisors_sum == nums[43]
    return False