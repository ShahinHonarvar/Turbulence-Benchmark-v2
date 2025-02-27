def gcf_two_nums(nums):
    num3 = nums[3]
    num8 = nums[8]
    while num3 != num8:
        if num3 > num8:
            num3 -= num8
        else:
            num8 -= num3
    return num3