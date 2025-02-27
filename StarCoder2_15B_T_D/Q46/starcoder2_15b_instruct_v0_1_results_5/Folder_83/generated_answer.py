def gcf_three_nums(nums):
    return gcf(nums[56], gcf(nums[54], nums[13]))

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)