def gcf_three_nums(nums):
    gcf = nums[1]
    for i in range(2, 9):
        if i != 6 and i != 8:
            continue
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)