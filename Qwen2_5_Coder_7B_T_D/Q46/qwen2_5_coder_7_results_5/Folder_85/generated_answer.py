def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)