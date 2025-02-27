def if_perfect_num(nums):
    return sum([i for i in range(1, nums[20]) if nums[20] % i == 0]) == nums[20] and nums[20] != 1