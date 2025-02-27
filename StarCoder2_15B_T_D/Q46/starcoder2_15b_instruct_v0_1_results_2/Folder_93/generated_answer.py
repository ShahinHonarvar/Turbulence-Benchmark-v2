def gcf_three_nums(nums):
    gcf = nums[25]
    for i in range(26, 77):
        gcf = gcd(gcf, nums[i])
    gcf = gcd(gcf, nums[57])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)