def gcf_three_nums(nums):
    num1 = nums[87]
    num2 = nums[20]
    num3 = nums[36]
    gcf = num1
    while num2 % gcf != 0 or num3 % gcf != 0:
        gcf -= 1
    return gcf