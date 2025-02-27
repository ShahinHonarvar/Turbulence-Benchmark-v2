def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[43], nums[99]) + 1):
        if nums[43] % i == 0 and nums[99] % i == 0:
            gcf = i
    return gcf