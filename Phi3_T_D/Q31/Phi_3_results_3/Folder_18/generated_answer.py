def if_perfect_num(nums):
    if len(nums) > 312:
        sum_factors = sum((i for i in range(1, nums[312]) if nums[312] % i == 0))
        return sum_factors == nums[312]
    return False