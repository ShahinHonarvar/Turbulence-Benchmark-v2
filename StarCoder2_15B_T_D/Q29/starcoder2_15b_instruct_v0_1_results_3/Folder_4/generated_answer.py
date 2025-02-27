def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[76], nums[57]) + 1):
        if nums[76] % i == 0 and nums[57] % i == 0:
            gcf = i
    return gcf