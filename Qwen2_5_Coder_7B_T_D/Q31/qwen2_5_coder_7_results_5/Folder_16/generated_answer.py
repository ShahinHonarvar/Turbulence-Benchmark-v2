def if_perfect_num(nums):
    return sum((nums[162] // i for i in range(1, nums[162]))) == nums[162] - 1