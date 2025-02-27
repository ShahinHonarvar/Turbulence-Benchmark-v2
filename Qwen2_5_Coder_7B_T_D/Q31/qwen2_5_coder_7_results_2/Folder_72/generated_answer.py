def if_perfect_num(nums):
    return sum([i for i in range(1, nums[16]) if nums[16] % i == 0]) == nums[16]