def if_perfect_num(nums):
    return nums[65] == sum([i for i in range(1, nums[65] // 2 + 1) if nums[65] % i == 0])