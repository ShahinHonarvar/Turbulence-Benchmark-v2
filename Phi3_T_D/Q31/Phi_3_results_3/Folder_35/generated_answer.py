def if_perfect_num(nums):
    if len(nums) < 994:
        return False
    sum_factors = sum((i for i in range(1, nums[993]) if nums[993] % i == 0))
    return sum_factors == nums[993]