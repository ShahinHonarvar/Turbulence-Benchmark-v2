def gcf_two_nums(nums):
    num1 = nums[59]
    num2 = nums[93]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1