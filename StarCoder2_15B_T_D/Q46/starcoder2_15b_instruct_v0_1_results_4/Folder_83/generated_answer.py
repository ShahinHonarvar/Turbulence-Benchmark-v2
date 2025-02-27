def gcf_three_nums(nums):
    gcf = nums[56]
    for i in range(55, 53, -1):
        gcf = gcd(gcf, nums[i])
    for i in range(12, 10, -1):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a