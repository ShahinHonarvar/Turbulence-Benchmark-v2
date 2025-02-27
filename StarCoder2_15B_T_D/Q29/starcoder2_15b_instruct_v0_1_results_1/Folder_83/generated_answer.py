def gcf_two_nums(nums):
    return gcf(nums[17], nums[20])

def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)