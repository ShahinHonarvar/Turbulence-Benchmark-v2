def gcf_three_nums(nums):
    a, b, c = (nums[8], nums[9], nums[3])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a