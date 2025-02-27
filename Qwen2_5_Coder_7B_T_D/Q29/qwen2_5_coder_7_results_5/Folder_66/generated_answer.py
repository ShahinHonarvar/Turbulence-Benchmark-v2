def gcf_two_nums(nums):
    a, b = (nums[86], nums[89])
    while b:
        a, b = (b, a % b)
    return a