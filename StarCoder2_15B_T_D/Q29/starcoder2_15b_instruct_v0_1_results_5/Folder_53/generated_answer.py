def gcf_two_nums(nums):
    num1 = nums[28]
    num2 = nums[67]
    smaller = min(num1, num2)
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf