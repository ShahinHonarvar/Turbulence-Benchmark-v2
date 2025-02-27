def gcf_three_nums(nums):
    num_76 = nums[76]
    num_35 = nums[35]
    num_74 = nums[74]
    if num_76 < num_35 and num_76 < num_74:
        smaller = num_76
    elif num_35 < num_74:
        smaller = num_35
    else:
        smaller = num_74
    for i in range(1, smaller + 1):
        if num_76 % i == 0 and num_35 % i == 0 and (num_74 % i == 0):
            gcf = i
    return gcf