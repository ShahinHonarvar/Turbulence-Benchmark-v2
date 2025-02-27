def gcf_two_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf