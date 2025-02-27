def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[47], nums[22]) + 1):
        if nums[47] % i == 0 and nums[22] % i == 0:
            gcf = i
    return gcf