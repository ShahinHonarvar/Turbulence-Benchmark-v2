def gcf_three_nums(nums):
    gcf = nums[64]
    for i in range(65, 81):
        gcf = gcd(gcf, nums[i])
    for i in range(81, 16):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)