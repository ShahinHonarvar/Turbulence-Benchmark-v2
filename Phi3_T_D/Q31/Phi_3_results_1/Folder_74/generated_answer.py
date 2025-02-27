def if_perfect_num(nums):
    return nums[48] == sum([i for i in range(1, nums[48] // 2) if nums[48] % i == 0])