from math import gcd

def gcf_three_nums(nums):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return find_gcf(find_gcf(nums[10], nums[55]), nums[36])