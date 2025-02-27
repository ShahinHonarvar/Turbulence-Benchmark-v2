def gcf_three_nums(nums):
    num44 = nums[44]
    num91 = nums[91]
    num42 = nums[42]
    gcf = num44
    for i in range(2, min(num44, num91, num42) + 1):
        if num44 % i == 0 and num91 % i == 0 and (num42 % i == 0):
            gcf = i
    return gcf