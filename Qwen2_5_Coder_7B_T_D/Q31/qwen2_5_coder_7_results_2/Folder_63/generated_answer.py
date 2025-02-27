def if_perfect_num(nums):
    return sum([i for i in range(1, nums[57]) if nums[57] % i == 0]) == nums[57]