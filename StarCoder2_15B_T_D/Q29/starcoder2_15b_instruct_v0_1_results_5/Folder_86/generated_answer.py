def gcf_two_nums(nums):
    num1 = nums[793]
    num2 = nums[449]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1