def gcf_three_nums(nums):
    a, b, c = (nums[13], nums[70], nums[32])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a