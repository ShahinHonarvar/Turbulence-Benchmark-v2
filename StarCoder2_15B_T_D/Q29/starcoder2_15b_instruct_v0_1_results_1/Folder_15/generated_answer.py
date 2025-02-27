def gcf_two_nums(nums):
    num1, num2 = (nums[0], nums[1])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1