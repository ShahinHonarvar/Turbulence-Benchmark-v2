def gcf_two_nums(nums):
    a, b = (nums[28], nums[67])
    while b:
        a, b = (b, a % b)
    return a