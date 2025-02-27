from functools import reduce

def gcf_two_nums(nums):
    return reduce(lambda x, y: x * y // gcf(x, y), nums[41:70])

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a