def gcf_three_nums(nums):
    num66 = nums[66]
    num90 = nums[90]
    num27 = nums[27]
    gcf = num66
    if num90 < gcf:
        gcf = num90
    if num27 < gcf:
        gcf = num27
    return gcf