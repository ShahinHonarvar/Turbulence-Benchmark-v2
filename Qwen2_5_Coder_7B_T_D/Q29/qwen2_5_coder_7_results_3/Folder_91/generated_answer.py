def gcf_two_nums(nums):
    return gcd(nums[0], nums[4])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a