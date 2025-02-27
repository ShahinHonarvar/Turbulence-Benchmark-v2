def gcf_three_nums(nums):
    gcf = nums[31]
    for i in range(31, 69):
        gcf = gcd(gcf, nums[i])
    gcf = gcd(gcf, nums[40])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a