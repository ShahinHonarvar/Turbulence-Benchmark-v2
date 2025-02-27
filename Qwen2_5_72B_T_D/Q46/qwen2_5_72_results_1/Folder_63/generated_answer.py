import math

def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[38], nums[52], nums[69])
    result = gcf(gcf(a, b), c)
    return result