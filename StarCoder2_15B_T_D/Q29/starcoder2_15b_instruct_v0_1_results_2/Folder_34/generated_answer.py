def gcf_two_nums(nums):
    num1 = nums[60]
    num2 = nums[64]
    if num2 > num1:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1