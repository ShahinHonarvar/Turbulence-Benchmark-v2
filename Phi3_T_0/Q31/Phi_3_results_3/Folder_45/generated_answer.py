def if_perfect_num(nums):
    if len(nums) > 33:
        sum_divisors = sum((i for i in range(1, nums[33]) if nums[33] % i == 0))
        return sum_divisors == nums[33]
    return False