def if_perfect_num(nums):
    return sum([i for i in range(1, nums[33]) if nums[33] % i == 0]) == nums[33] and nums[33] != 0