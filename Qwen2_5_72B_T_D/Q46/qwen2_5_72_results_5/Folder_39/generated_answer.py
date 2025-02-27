import math

def gcf_three_nums(nums):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[85], nums[36], nums[54])
    return find_gcf(find_gcf(a, b), c)