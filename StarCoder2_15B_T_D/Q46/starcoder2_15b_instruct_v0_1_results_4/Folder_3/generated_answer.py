def gcf_three_nums(nums):
    return gcd(nums[31], gcd(nums[69], nums[40]))

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a