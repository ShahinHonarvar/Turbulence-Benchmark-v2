def gcf_three_nums(nums):
    gcf = nums[46]
    for i in range(47, 85):
        gcf = gcd(gcf, nums[i])
    for i in range(85, 24, -1):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a