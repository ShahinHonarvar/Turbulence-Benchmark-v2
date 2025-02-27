def if_perfect_num(nums):
    return sum((nums[47] // i for i in range(1, nums[47]))) == nums[47] and nums[47] != 1