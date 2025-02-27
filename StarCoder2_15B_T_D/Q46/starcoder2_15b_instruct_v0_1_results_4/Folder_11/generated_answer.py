def gcf_three_nums(nums):
    num1 = nums[37]
    num2 = nums[30]
    num3 = nums[48]
    gcf = num1
    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf