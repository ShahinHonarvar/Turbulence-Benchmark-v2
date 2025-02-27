def gcf_three_nums(nums):
    gcf = nums[412]
    for i in range(413, 933):
        gcf = gcd(gcf, nums[i])
    for i in range(933, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)