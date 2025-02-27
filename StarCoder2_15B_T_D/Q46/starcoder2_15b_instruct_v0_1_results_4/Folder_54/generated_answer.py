def gcf_three_nums(nums):
    gcf = nums[96]
    for i in range(96, 85, -1):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)