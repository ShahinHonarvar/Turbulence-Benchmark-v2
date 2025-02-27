def gcf_three_nums(nums):
    a, b, c = (nums[17], nums[88], nums[35])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a