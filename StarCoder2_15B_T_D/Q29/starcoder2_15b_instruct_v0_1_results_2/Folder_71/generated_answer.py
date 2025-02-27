def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[78], nums[93]) + 1):
        if nums[78] % i == 0 and nums[93] % i == 0:
            gcf = i
    return gcf