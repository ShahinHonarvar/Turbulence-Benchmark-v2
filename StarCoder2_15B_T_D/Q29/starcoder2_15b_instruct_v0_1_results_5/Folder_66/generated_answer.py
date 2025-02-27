def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[86], nums[89]) + 1):
        if nums[86] % i == 0 and nums[89] % i == 0:
            gcf = i
    return gcf