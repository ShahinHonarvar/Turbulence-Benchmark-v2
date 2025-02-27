def gcf_three_nums(nums):
    return gcf(nums[0], gcf(nums[8], nums[3]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a