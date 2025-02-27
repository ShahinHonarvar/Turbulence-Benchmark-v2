def gcf_three_nums(nums):
    num_20 = nums[20]
    num_17 = nums[17]
    num_28 = nums[28]
    gcf = 1
    for i in range(2, min(num_20, num_17, num_28) + 1):
        if num_20 % i == 0 and num_17 % i == 0 and (num_28 % i == 0):
            gcf = i
    return gcf