def gcf_two_nums(nums):
    a, b = (nums[49], nums[31])
    while b:
        a, b = (b, a % b)
    return a