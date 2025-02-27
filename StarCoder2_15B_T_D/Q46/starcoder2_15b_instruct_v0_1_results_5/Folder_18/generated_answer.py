def gcf_three_nums(nums):
    return gcd(nums[637], gcd(nums[411], nums[757]))

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a