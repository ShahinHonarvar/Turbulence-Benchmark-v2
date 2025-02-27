from math import gcd

def gcf_three_nums(nums):

    def find_gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return find_gcd(nums[92], find_gcd(nums[69], nums[95]))