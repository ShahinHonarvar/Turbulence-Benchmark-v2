def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < max(40, 15, 99):
        return None
    return gcd(gcd(nums[40], nums[15]), nums[99])