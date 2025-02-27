def gcf_two_nums(nums):
    num_1 = nums[36]
    num_2 = nums[85]
    smaller = min(num_1, num_2)
    for i in range(smaller, 0, -1):
        if num_1 % i == 0 and num_2 % i == 0:
            return i
    return 1