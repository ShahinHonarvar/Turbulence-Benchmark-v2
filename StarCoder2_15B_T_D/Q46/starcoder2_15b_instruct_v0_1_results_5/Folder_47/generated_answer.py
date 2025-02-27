def gcf_three_nums(nums):
    num_36 = nums[36]
    num_85 = nums[85]
    num_83 = nums[83]
    gcf = num_36
    if num_85 < gcf:
        gcf = num_85
    if num_83 < gcf:
        gcf = num_83
    return gcf