def gcf_two_nums(nums):
    if len(nums) > 64:
        num1 = nums[64]
        num2 = nums[28]
    else:
        num1 = nums[-1]
        num2 = nums[-2]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf