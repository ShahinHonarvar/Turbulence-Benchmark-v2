def if_perfect_num(nums):
    if len(nums) > 60:
        sum_divisors = sum((i for i in range(1, nums[60]) if nums[60] % i == 0))
        return sum_divisors == nums[60]
    return False