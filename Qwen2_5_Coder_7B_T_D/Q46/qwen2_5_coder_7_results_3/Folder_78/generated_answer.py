def gcf_three_nums(nums):
    a = nums[13]
    b = nums[70]
    c = nums[32]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a