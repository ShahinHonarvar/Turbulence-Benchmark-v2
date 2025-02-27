def gcf_three_nums(nums):
    gcf = nums[64]
    for i in range(65, 81):
        gcf = gcd(gcf, nums[i])
    for i in range(81, 16):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a