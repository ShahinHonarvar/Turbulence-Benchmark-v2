def gcf_three_nums(nums):
    nine6 = nums[96]
    five7 = nums[57]
    eight5 = nums[85]
    while five7 != eight5:
        if five7 > eight5:
            five7 -= eight5
        else:
            eight5 -= five7
    while nine6 != five7:
        if nine6 > five7:
            nine6 -= five7
        else:
            five7 -= nine6
    return five7