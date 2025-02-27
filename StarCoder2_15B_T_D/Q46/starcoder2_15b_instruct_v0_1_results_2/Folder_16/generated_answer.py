def gcf_three_nums(nums):
    return gcf(nums[558], gcf(nums[110], nums[628]))

def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)