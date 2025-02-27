def gcf_two_nums(nums):
    return gcd(nums[18], nums[37])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a