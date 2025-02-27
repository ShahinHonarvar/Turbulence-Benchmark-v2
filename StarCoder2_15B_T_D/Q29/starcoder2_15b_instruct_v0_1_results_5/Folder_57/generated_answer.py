def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[49]
    if num1 == 0:
        return num2
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1