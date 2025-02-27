def gcf_three_nums(nums):
    return gcf(nums[21], nums[69], nums[41])

def gcf(a, b, c):
    return gcd(gcd(a, b), c)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)