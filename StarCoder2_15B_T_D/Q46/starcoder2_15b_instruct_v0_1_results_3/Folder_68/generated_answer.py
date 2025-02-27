def gcf_three_nums(nums):
    gcf = nums[4]
    for i in range(1, 8):
        if i != 4:
            gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a