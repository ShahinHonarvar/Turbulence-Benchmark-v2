def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]
    gcf = num1
    for i in range(2, min(num2, num3) + 1):
        if num2 % i == 0 and num3 % i == 0:
            gcf = i
    return gcf