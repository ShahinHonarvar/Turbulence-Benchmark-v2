def gcf_three_nums(nums):
    num1, num2, num3 = (nums[10], nums[55], nums[36])
    gcf = min(num1, num2, num3)
    while not num1 % gcf == num2 % gcf == num3 % gcf == 0:
        gcf -= 1
    return gcf