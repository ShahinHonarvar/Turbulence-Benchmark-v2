def gcf_three_nums(nums):
    a, b, c = (nums[56], nums[54], nums[13])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a