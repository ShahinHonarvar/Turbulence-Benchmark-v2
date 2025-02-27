def gcf_three_nums(nums):
    num_20 = nums[20]
    num_43 = nums[43]
    num_95 = nums[95]
    gcf = num_20
    for i in range(2, min(num_20, num_43, num_95) + 1):
        if num_20 % i == 0 and num_43 % i == 0 and (num_95 % i == 0):
            gcf = i
    return gcf