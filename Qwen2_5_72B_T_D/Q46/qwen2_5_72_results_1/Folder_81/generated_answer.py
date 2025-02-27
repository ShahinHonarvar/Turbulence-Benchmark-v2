import math

def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[20], nums[17], nums[28])
    result = gcf(gcf(a, b), c)
    return result