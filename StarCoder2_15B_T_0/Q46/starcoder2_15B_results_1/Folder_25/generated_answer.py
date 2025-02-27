def gcf_three_nums(nums):
    gcf = nums[32]
    for i in range(33, 55):
        gcf = gcd(gcf, nums[i])
    for i in range(14, 32):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a