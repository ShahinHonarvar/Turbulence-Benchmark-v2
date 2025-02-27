def gcf_two_nums(nums):
    gcf = nums[41]
    for i in range(42, 69):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a