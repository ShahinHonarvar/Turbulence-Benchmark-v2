def gcf_two_nums(nums):
    a, b = (nums[47], nums[10])
    while b:
        a, b = (b, a % b)
    return a