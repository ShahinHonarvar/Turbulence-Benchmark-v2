def gcf_two_nums(nums):
    num_48 = nums[48]
    num_74 = nums[74]
    smaller = min(num_48, num_74)
    for i in range(smaller, 0, -1):
        if num_48 % i == 0 and num_74 % i == 0:
            return i