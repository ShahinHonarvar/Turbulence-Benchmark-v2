def gcf_two_nums(nums):
    a, b = (nums[43], nums[99])
    while b:
        a, b = (b, a % b)
    return a