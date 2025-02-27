def gcf_three_nums(nums):
    num1 = nums[44]
    num2 = nums[91]
    num3 = nums[42]
    gcf = num1
    while gcf != num2 and gcf != num3:
        gcf -= 1
    return gcf