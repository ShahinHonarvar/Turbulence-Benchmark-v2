def if_perfect_num(nums):
    return sum([i for i in range(1, nums[74]) if nums[74] % i == 0]) == nums[74]