def gcf_two_nums(nums):
    num_894 = nums[894]
    num_801 = nums[801]
    if num_894 > num_801:
        smaller = num_801
    else:
        smaller = num_894
    for i in range(1, smaller + 1):
        if num_894 % i == 0 and num_801 % i == 0:
            gcf = i
    return gcf