def gcf_three_nums(lst):
    nums = sorted([lst[654], lst[312], lst[441]])
    smaller = nums[0]
    larger = nums[1]
    while larger % smaller != 0:
        smaller, larger = (larger % smaller, smaller)
    return gcd(larger, nums[2])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a