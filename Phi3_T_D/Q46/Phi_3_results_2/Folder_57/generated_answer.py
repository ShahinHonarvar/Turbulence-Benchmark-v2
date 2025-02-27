def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(nums[90], gcd(nums[41], nums[95]))