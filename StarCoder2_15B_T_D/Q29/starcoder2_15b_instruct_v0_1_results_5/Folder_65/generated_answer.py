def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[29], nums[53]) + 1):
        if nums[29] % i == 0 and nums[53] % i == 0:
            gcf = i
    return gcf