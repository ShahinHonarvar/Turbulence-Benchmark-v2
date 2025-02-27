def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[46], nums[13]) + 1):
        if nums[46] % i == 0 and nums[13] % i == 0:
            gcf = i
    return gcf