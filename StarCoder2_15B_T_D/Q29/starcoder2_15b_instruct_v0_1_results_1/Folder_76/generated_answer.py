def gcf_two_nums(nums):
    num1 = nums[184]
    num2 = nums[307]
    num1, num2 = sorted([num1, num2])
    while num2 > 0:
        num1, num2 = (num2, num1 % num2)
    return num1