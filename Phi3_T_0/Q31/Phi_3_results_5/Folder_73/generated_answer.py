def if_perfect_num(nums):
    if len(nums) > 41:
        divisors_sum = sum((i for i in range(1, nums[41]) if nums[41] % i == 0))
        return divisors_sum == nums[41]
    return False