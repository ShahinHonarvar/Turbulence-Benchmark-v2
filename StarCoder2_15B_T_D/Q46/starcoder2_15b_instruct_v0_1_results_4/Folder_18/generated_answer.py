def gcf_three_nums(nums):
    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]
    gcf = num1
    while gcf != num2 and gcf != num3:
        gcf -= 1
    return gcf