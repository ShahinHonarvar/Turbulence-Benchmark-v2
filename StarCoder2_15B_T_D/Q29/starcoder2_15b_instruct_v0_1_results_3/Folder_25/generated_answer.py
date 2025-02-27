def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[41], nums[69]) + 1):
        if nums[41] % i == 0 and nums[69] % i == 0:
            gcf = i
    return gcf