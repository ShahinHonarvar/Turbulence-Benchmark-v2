def gcf_three_nums(nums):
    a = nums[96]
    b = nums[57]
    c = nums[85]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a