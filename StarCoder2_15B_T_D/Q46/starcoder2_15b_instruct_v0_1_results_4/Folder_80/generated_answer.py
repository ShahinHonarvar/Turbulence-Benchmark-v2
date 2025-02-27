def gcf_three_nums(nums):
    num1 = nums[13]
    num2 = nums[76]
    num3 = nums[44]
    gcf = num1
    for i in range(2, min(num2, num3) + 1):
        if num2 % i == 0 and num3 % i == 0:
            gcf = i
    return gcf