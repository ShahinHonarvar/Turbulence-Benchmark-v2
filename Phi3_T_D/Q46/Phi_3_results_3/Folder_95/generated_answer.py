from math import gcd

def gcf_three_nums(nums):

    def get_gcd(a, b, c):
        return gcd(gcd(a, b), c)
    indices = [87, 20, 36]
    return get_gcd(nums[indices[0]], nums[indices[1]], nums[indices[2]])