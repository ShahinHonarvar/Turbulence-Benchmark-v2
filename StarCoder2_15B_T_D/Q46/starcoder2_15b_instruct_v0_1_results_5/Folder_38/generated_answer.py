def gcf_three_nums(nums):
    return gcf(nums[14], gcf(nums[21], nums[17]))

def gcf(x, y):
    while y != 0:
        x, y = (y, x % y)
    return x