def if_perfect_num(nums):
    if len(nums) > 48:
        divisors_sum = sum((i for i in range(1, nums[48]) if nums[48] % i == 0))
        return divisors_sum == nums[48]
    return False