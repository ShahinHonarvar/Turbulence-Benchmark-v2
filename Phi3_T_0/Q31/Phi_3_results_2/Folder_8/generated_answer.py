def if_perfect_num(nums):
    if len(nums) > 49:
        return sum([i for i in range(1, nums[49]) if nums[49] % i == 0]) == nums[49]
    return False