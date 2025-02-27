def gcf_two_nums(nums):
    num_1 = nums[36]
    num_2 = nums[85]
    if num_1 > num_2:
        smaller_num = num_2
    else:
        smaller_num = num_1
    for i in range(1, smaller_num + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcf = i
    return gcf