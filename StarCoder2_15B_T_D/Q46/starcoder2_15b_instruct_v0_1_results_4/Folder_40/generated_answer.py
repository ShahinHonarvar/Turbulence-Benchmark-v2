def gcf_three_nums(nums):
    gcf = nums[1]
    for i in range(1, 9):
        if i != 6 and i != 8:
            continue
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a