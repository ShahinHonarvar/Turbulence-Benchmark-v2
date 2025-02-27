def gcf_three_nums(nums):
    a = nums[21]
    b = nums[51]
    c = nums[33]
    return gcf(gcf(a, b), c)

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a