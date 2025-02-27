def gcf_two_nums(nums):
    num1 = nums[85]
    num2 = nums[33]
    gcf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf