def gcf_three_nums(nums):
    return gcf(nums[13], gcf(nums[76], nums[44]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a