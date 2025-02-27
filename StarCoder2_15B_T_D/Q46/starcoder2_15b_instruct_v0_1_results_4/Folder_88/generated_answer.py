def gcf_three_nums(nums):
    return gcf(nums[47], gcf(nums[10], nums[28]))

def gcf(x, y):
    while y != 0:
        x, y = (y, x % y)
    return x