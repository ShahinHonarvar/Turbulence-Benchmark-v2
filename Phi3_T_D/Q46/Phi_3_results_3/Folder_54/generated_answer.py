def gcf_three_nums(nums):
    a, b, c = (nums[95], nums[56], nums[84])

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)