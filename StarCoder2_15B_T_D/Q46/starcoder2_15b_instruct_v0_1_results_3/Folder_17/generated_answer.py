def gcf_three_nums(nums):
    num20 = nums[20]
    num51 = nums[51]
    num62 = nums[62]
    gcf = num20
    if num51 < gcf:
        gcf = num51
    if num62 < gcf:
        gcf = num62
    return gcf