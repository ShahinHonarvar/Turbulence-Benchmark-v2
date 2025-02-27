def gcf_two_nums(nums):
    num1 = nums[87]
    num2 = nums[95]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1