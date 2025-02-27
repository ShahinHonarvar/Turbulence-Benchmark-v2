def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[279], nums[812]) + 1):
        if nums[279] % i == 0 and nums[812] % i == 0:
            gcf = i
    return gcf