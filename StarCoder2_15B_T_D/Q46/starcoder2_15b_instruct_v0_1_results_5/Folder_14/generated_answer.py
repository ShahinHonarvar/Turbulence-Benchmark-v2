def gcf_three_nums(nums):
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]
    if num1 == 0:
        return num2
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    gcf = num1
    for i in range(2, gcf + 1):
        if num2 % i == 0 and num3 % i == 0:
            gcf = i
            break
    return gcf