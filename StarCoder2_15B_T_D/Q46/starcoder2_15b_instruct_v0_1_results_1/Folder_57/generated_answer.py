def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    if a == 0:
        return b
    while b != 0:
        a, b = (b, a % b)
    if c == 0:
        return a
    while c != 0:
        b, c = (c, b % c)
    return c