def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    while b != 0:
        a, b = (b, a % b)
    gcf = a
    while c != 0:
        gcf, c = (c, gcf % c)
    return gcf