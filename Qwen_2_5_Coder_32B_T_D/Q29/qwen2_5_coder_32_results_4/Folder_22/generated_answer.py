def gcf_two_nums(nums):
    a, b = (nums[24], nums[68])
    while b:
        a, b = (b, a % b)
    return a