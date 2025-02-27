def gcf_two_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return gcf_two_nums([num1 - num2, num2])
    else:
        return gcf_two_nums([num1, num2 - num1])