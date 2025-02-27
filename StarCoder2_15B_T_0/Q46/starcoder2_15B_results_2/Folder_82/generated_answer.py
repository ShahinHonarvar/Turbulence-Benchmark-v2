def gcf_three_nums(nums):
    gcf = nums[67]
    for i in range(68, 85):
        gcf = gcd(gcf, nums[i])
    for i in range(85, 14, -1):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a