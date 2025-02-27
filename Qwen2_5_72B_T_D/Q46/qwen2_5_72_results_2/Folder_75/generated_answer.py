from math import gcd

def gcf_three_nums(nums):

    def find_gcf(x, y):
        return gcd(x, y)
    a, b, c = (nums[70], nums[98], nums[22])
    gcf_ab = find_gcf(a, b)
    gcf_abc = find_gcf(gcf_ab, c)
    return gcf_abc