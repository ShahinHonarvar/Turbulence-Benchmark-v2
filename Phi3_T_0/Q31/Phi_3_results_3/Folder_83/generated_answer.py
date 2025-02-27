def if_perfect_num(nums):
    if len(nums) > 95:
        sum_divisors = sum((i for i in range(1, nums[95]) if nums[95] % i == 0))
        return sum_divisors == nums[95]
    return False