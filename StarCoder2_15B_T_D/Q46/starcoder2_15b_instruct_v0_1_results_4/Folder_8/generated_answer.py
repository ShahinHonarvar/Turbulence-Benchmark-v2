def gcf_three_nums(nums):
    gcf = nums[99]
    for i in range(28, 54):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)