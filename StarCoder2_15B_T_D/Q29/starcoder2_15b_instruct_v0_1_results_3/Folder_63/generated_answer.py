def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[21], nums[17]) + 1):
        if nums[21] % i == 0 and nums[17] % i == 0:
            gcf = i
    return gcf