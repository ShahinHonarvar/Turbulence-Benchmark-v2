def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[64], nums[80]) + 1):
        if nums[64] % i == 0 and nums[80] % i == 0:
            gcf = i
    return gcf