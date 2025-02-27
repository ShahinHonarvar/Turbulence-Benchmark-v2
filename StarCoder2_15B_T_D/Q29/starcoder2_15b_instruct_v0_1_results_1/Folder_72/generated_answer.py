def gcf_two_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        while num2 != 0:
            remainder = num1 % num2
            num1 = num2
            num2 = remainder
        return num1