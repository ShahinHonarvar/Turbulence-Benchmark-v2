def if_perfect_num(nums):
    if len(nums) > 37:
        return sum([i for i in range(1, nums[37]) if nums[37] % i == 0]) == nums[37]
    return False