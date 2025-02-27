def gcf_two_nums(nums):
    num1 = nums[20]
    num2 = nums[83]
    smaller = min(num1, num2)
    gcf = 1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf