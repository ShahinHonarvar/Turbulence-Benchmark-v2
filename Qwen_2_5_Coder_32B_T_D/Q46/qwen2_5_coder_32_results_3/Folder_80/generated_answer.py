def gcf_three_nums(nums):
    a, b, c = (nums[13], nums[76], nums[44])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a