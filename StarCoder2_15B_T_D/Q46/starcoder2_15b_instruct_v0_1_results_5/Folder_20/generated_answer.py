def gcf_three_nums(nums):
    num_29 = nums[29]
    num_53 = nums[53]
    num_42 = nums[42]
    gcf = num_29
    for i in range(2, min(num_29, num_53, num_42) + 1):
        if num_29 % i == 0 and num_53 % i == 0 and (num_42 % i == 0):
            gcf = i
    return gcf