def gcf_three_nums(nums):
    return gcf(nums[18], gcf(nums[37], nums[43]))

def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)