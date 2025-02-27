def if_perfect_num(nums):
    return nums[37] == sum([i for i in range(1, nums[37]) if nums[37] % i == 0])