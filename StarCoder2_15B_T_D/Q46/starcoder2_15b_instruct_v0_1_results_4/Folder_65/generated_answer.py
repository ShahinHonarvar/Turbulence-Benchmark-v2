def gcf_three_nums(nums):
    num1 = nums[18]
    num2 = nums[10]
    num3 = nums[76]
    gcf = min(num1, num2, num3)
    while num1 % gcf != 0 or num2 % gcf != 0 or num3 % gcf != 0:
        gcf -= 1
    return gcf