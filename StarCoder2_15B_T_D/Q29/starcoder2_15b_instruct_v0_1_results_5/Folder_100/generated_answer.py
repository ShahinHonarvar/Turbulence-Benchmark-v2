def gcf_two_nums(nums):
    num_1 = nums[96]
    num_2 = nums[32]
    gcf = 1
    for i in range(2, min(num_1, num_2) + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcf = i
    return gcf