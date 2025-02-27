def if_perfect_num(nums):
    if len(nums) > 64:
        return sum([i for i in range(1, nums[64]) if nums[64] % i == 0]) == nums[64]
    return False