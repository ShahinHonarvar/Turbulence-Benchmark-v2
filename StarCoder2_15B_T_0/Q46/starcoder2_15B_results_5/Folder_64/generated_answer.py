def gcf_three_nums(nums):
    gcf = nums[0]
    for i in range(1, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)