def gcf_three_nums(nums):
    a = nums[15]
    b = nums[51]
    c = nums[76]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)