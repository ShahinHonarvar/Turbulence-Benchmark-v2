def if_perfect_num(nums):
    return sum((nums[68] // i for i in range(1, nums[68]) if nums[68] % i == 0)) == nums[68] and nums[68] != 1