def gcf_two_nums(nums):
    num1 = nums[69]
    num2 = nums[41]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1