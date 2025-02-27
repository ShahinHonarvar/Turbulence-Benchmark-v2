def gcf_three_nums(nums):
    gcf = nums[63]
    for i in range(64, 74):
        gcf = gcd(gcf, nums[i])
    gcf = gcd(gcf, nums[11])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a