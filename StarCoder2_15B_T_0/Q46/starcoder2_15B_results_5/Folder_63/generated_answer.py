def gcf_three_nums(nums):
    gcf = nums[38]
    for i in range(39, 69):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a