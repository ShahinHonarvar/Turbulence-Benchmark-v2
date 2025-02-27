def gcf_two_nums(nums):
    a, b = (nums[60], nums[64])
    while b:
        a, b = (b, a % b)
    return a