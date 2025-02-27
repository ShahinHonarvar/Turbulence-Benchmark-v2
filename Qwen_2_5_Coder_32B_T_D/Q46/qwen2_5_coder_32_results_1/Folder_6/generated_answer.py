def gcf_three_nums(nums):
    a, b, c = (nums[93], nums[94], nums[57])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a