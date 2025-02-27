def gcf_three_nums(nums):
    num1 = nums[1]
    num2 = nums[6]
    num3 = nums[8]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    gcf = num1
    while gcf != num3:
        if gcf > num3:
            gcf -= num3
        else:
            num3 -= gcf
    return gcf