def gcf_three_nums(nums):
    return gcd(gcd(nums[27], nums[85]), nums[51])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a