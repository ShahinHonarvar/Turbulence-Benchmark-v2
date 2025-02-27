def gcf_two_nums(nums):
    a, b = (nums[4], nums[0])
    while b:
        a, b = (b, a % b)
    return a