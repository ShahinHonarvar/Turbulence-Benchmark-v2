def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    while b != 0:
        a, b = (b, a % b)
    gcf = a
    while c != 0:
        gcf, c = (c, gcf % c)
    return gcf