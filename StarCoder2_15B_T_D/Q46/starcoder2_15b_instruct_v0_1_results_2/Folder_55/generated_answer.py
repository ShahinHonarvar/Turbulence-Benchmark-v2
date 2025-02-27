def gcf_three_nums(nums):
    n9 = nums[9]
    n6 = nums[6]
    n2 = nums[2]
    gcf = n9
    while gcf % n6 != 0 or gcf % n2 != 0:
        gcf -= 1
    return gcf