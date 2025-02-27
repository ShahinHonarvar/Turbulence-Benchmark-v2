def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        return gcd(gcd(a, b), c)
    if len(nums) < 58:
        return None
    return gcf(nums[25], nums[76], nums[57])