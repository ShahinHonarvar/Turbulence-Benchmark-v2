def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[60], nums[64]) + 1):
        if nums[60] % i == 0 and nums[64] % i == 0:
            gcf = i
    return gcf