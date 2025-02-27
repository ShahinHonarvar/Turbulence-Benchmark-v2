def gcf_two_nums(nums):
    a, b = (nums[88], nums[35])
    while b:
        a, b = (b, a % b)
    return a