def gcf_three_nums(nums: list) -> int:
    gcf = nums[19]
    for i in range(19 + 1, 49):
        gcf = gcd(gcf, nums[i])
    for i in range(49 + 1, 74):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a