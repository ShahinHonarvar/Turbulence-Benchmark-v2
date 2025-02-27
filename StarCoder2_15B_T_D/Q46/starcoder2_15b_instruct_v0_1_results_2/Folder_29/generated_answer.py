def gcf_three_nums(nums: list) -> int:
    gcf = nums[22]
    for i in range(23, 98):
        gcf = gcd(gcf, nums[i])
    return gcf

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)