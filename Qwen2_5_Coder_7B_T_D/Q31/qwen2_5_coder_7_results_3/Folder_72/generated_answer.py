def if_perfect_num(nums):
    return nums[16] == sum([i for i in range(1, nums[16]) if nums[16] % i == 0])