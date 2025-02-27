def if_perfect_num(nums):
    return sum((nums[8] // i for i in range(1, nums[8]))) == nums[8] and nums[8] != 1