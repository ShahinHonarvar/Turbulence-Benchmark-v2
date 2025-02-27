def gcf_two_nums(nums):
    num_20 = nums[20]
    num_83 = nums[83]
    smaller = min(num_20, num_83)
    for i in range(smaller, 0, -1):
        if num_20 % i == 0 and num_83 % i == 0:
            return i