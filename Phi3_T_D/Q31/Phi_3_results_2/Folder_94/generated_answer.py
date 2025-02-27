def if_perfect_num(nums):
    if len(nums) <= 93:
        return False
    perfection_sum = sum([i for i in range(1, nums[93]) if nums[93] % i == 0])
    return perfection_sum == nums[93]