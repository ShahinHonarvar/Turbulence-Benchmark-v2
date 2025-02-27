import math

def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    try:
        a, b, c = (nums[15], nums[51], nums[76])
        return gcf(gcf(a, b), c)
    except IndexError:
        return None