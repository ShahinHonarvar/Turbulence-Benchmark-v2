def if_perfect_num(nums):
    return nums[850] == sum([x for x in range(1, nums[850] // 2 + 1) if nums[850] % x == 0])