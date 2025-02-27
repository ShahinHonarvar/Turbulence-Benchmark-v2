def if_perfect_num(nums):
    return sum([d for d in range(1, nums[24]) if nums[24] % d == 0]) == nums[24]