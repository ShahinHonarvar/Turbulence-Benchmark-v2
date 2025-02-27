def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[85], nums[51]) + 1):
        if nums[85] % i == 0 and nums[51] % i == 0:
            gcf = i
    return gcf