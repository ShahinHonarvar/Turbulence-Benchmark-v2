def gcf_two_nums(nums):
    a, b = (nums[69], nums[41])
    while b:
        a, b = (b, a % b)
    return a