def gcf_three_nums(nums):
    a = nums[74]
    b = nums[60]
    c = nums[28]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        b, c = (c, b % c)
    return c