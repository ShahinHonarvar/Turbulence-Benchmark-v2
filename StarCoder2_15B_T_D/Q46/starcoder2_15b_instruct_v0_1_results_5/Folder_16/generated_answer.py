def gcf_three_nums(nums):
    num1 = nums[558]
    num2 = nums[110]
    num3 = nums[628]
    gcf = num1
    while gcf != num2 and gcf != num3:
        gcf -= 1
    return gcf