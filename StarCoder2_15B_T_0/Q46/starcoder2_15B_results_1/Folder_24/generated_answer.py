def gcf_three_nums(nums):
    gcf = nums[18]
    for i in range(19, 44):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a