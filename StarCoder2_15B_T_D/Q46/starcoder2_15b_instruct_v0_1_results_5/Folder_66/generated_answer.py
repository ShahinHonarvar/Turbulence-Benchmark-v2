def gcf_three_nums(nums):
    num1 = nums[92]
    num2 = nums[69]
    num3 = nums[95]
    gcf = min(num1, num2, num3)
    while not (num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0)):
        gcf -= 1
    return gcf