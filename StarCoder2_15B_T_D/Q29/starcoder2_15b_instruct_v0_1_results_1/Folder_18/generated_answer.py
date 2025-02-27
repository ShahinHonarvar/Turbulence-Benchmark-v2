def gcf_two_nums(nums):
    num1 = nums[872]
    num2 = nums[219]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1