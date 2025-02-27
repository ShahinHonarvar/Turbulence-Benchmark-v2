def gcf_three_nums(nums):
    gcf = nums[34]
    for i in range(35, 39):
        gcf = gcd(gcf, nums[i])
    for i in range(78, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a