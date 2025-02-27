def gcf_two_nums(nums):
    num1 = nums[15]
    num2 = nums[40]
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1