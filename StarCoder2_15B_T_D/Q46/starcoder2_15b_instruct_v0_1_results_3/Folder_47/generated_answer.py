def gcf_three_nums(nums):
    gcf = nums[36]
    for i in range(36, 86):
        if i == 36:
            continue
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)