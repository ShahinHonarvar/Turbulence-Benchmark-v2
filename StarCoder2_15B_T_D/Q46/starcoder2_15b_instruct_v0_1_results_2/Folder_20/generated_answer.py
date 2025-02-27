def gcf_three_nums(nums):
    return gcd(nums[29], gcd(nums[53], nums[42]))

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a