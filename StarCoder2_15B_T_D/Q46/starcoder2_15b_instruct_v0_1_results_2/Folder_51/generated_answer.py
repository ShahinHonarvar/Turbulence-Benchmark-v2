def gcf_three_nums(nums):
    a = nums[21]
    b = nums[69]
    c = nums[41]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a