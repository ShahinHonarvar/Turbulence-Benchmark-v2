def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[15], nums[40]) + 1):
        if nums[15] % i == 0 and nums[40] % i == 0:
            gcf = i
    return gcf