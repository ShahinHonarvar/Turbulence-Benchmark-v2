def if_perfect_num(nums):
    return sum([i for i in range(1, nums[10]) if nums[10] % i == 0]) == nums[10]