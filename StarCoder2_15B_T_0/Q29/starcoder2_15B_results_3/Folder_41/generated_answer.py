def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[23], nums[27]) + 1):
        if nums[23] % i == 0 and nums[27] % i == 0:
            gcf = i
    return gcf