def if_perfect_num(nums):
    if len(nums) > 46:
        divisors_sum = sum((i for i in range(1, nums[46]) if nums[46] % i == 0))
        return divisors_sum == nums[46]
    return False