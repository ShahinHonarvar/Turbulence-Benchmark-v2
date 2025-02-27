def gcf_three_nums(nums):
    a, b, c = (nums[34], nums[38], nums[77])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a