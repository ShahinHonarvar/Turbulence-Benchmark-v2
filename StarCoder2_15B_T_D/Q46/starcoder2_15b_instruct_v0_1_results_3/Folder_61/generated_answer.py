def gcf_three_nums(nums):
    a = nums[1]
    b = nums[2]
    c = nums[7]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a