import math

def gcf_three_nums(nums):

    def gcf(a, b):
        return math.gcd(a, b)

    def gcf_three(a, b, c):
        return gcf(gcf(a, b), c)
    return gcf_three(nums[1], nums[6], nums[8])