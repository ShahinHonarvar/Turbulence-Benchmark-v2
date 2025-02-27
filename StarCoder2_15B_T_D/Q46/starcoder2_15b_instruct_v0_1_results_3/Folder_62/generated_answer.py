def gcf_three_nums(nums):
    return gcf(nums[10], gcf(nums[55], nums[36]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a