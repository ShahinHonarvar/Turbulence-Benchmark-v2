def gcf_three_nums(nums):
    num20 = nums[20]
    num43 = nums[43]
    num95 = nums[95]
    gcf = num20
    for i in range(2, min(num20, num43, num95) + 1):
        if num20 % i == 0 and num43 % i == 0 and (num95 % i == 0):
            gcf = i
    return gcf