def gcf_three_nums(nums):
    a, b, c = (nums[252], nums[149], nums[564])
    while b:
        a, b = (b, a % b)
    return a