def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcf(gcf(nums[742], nums[888]), nums[629])