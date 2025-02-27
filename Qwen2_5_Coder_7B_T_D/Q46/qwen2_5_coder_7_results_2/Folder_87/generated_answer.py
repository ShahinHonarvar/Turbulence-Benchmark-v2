def gcf_three_nums(nums):
    return gcd(gcd(nums[74], nums[60]), nums[28])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a