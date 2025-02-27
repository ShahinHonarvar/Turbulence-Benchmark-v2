def gcf_two_nums(nums):
    return gcf(nums[33], nums[72])

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a