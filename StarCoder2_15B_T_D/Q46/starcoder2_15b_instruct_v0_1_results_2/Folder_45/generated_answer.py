def gcf_three_nums(nums):
    return gcf(nums[46], nums[84], nums[23])

def gcf(a, b, c):
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a