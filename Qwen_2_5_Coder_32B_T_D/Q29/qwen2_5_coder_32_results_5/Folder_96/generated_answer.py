def gcf_two_nums(nums):
    a, b = (nums[95], nums[73])
    while b:
        a, b = (b, a % b)
    return a