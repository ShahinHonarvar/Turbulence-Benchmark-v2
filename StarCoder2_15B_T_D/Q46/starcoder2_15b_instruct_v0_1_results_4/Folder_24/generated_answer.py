def gcf_three_nums(nums):
    a = nums[18]
    b = nums[37]
    c = nums[43]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a