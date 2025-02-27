def gcf_three_nums(nums):
    a = nums[20]
    b = nums[43]
    c = nums[95]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a