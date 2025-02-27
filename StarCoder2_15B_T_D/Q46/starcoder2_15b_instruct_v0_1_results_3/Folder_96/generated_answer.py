def gcf_three_nums(nums):
    num29 = nums[29]
    num74 = nums[74]
    num49 = nums[49]
    gcf = num29
    if num74 < gcf:
        gcf = num74
    if num49 < gcf:
        gcf = num49
    return gcf