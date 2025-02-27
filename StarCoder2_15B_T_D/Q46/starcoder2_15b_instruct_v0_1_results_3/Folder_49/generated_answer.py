def gcf_three_nums(nums):
    return gcd(nums[34], nums[38], nums[77])

def gcd(a, b, c):
    return gcd(gcd(a, b), c)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)