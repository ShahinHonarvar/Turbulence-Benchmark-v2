def gcf_three_nums(nums):
    a, b, c = (nums[36], nums[85], nums[83])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a