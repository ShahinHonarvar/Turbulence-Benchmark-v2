def gcf_three_nums(nums):
    a, b, c = (nums[78], nums[19], nums[13])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        b, c = (c, b % c)
    return c