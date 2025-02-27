def gcf_two_nums(nums):
    gcf = 1
    for i in range(2, min(nums[534], nums[630]) + 1):
        if nums[534] % i == 0 and nums[630] % i == 0:
            gcf = i
    return gcf