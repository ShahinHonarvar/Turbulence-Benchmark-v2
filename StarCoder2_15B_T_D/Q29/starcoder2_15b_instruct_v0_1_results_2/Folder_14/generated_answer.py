def gcf_two_nums(nums):
    num1 = nums[49]
    num2 = nums[53]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        remainder = num1 % num2
        while remainder != 0:
            num1 = num2
            num2 = remainder
            remainder = num1 % num2
        return num2