def gcf_three_nums(nums):
    gcf = nums[47]
    for i in range(10, 29):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)