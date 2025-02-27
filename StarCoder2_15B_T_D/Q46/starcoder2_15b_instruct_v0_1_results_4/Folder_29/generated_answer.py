def gcf_three_nums(nums):
    num1 = nums[22]
    num2 = nums[97]
    num3 = nums[64]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    gcf = num1
    while num3 % gcf != 0:
        gcf = num3 % gcf
    return gcf