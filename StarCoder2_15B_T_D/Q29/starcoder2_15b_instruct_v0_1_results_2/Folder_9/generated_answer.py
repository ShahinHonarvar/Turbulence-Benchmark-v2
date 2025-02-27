def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[84], nums[63]) + 1):
        if nums[84] % i == 0 and nums[63] % i == 0:
            gcf = i
    return gcf