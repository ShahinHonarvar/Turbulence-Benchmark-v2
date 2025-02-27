from functools import reduce

def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 28:
        return None
    factor = gcd(nums[23], nums[27])
    return factor