def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a