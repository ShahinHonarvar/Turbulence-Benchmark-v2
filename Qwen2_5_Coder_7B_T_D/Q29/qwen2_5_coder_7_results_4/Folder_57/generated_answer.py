def gcf_two_nums(nums):
    return gcd(nums[28], nums[49])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a