def gcf_three_nums(nums):
    num_20 = nums[20]
    num_35 = nums[35]
    num_74 = nums[74]
    gcf = num_20
    for i in range(2, min(num_20, num_35, num_74) + 1):
        if num_20 % i == 0 and num_35 % i == 0 and (num_74 % i == 0):
            gcf = i
    return gcf