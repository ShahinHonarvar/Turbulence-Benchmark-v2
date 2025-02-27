def gcf_three_nums(nums):
    num_66 = nums[66]
    num_90 = nums[90]
    num_27 = nums[27]
    while num_66 != num_90:
        if num_66 > num_90:
            num_66 -= num_90
        else:
            num_90 -= num_66
    gcf = num_66
    while num_27 != gcf:
        if num_27 > gcf:
            num_27 -= gcf
        else:
            gcf -= num_27
    return gcf