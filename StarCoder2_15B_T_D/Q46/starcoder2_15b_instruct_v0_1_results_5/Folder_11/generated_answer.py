def gcf_three_nums(nums):
    n37 = nums[37]
    n30 = nums[30]
    n48 = nums[48]
    gcf = n37
    while gcf % n30 != 0 or gcf % n48 != 0:
        gcf -= 1
    return gcf