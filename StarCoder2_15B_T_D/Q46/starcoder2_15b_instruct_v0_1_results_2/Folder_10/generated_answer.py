def gcf_three_nums(nums):
    a = nums[86]
    b = nums[89]
    c = nums[49]
    while b != 0:
        a, b = (b, a % b)
    gcf = a
    while c != 0:
        gcf, c = (c, gcf % c)
    return gcf