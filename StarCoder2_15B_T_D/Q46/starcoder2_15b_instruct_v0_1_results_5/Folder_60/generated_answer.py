def gcf_three_nums(nums):
    return gcf(nums[96], gcf(nums[53], nums[35]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a