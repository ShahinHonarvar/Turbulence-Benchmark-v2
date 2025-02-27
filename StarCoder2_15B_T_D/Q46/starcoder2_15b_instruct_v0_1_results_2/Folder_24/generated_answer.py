def gcf_three_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]
    gcf = num1
    if num2 < gcf:
        gcf = num2
    if num3 < gcf:
        gcf = num3
    return gcf