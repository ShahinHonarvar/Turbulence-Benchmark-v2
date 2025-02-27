def gcf_two_nums(nums):
    num1 = nums[18]
    num2 = nums[37]
    smaller = min(num1, num2)
    gcf = 1
    for i in range(2, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf