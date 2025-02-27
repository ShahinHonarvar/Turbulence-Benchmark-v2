def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[83], nums[14]) + 1):
        if nums[83] % i == 0 and nums[14] % i == 0:
            gcf = i
    return gcf