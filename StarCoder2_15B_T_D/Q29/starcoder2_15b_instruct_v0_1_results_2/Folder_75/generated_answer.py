def gcf_two_nums(nums):
    num_42 = nums[42]
    num_25 = nums[25]
    if num_42 < num_25:
        smaller = num_42
    else:
        smaller = num_25
    for i in range(1, smaller + 1):
        if num_42 % i == 0 and num_25 % i == 0:
            gcf = i
    return gcf