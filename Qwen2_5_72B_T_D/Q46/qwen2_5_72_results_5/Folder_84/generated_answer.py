def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[695], nums[710], nums[914])
    return gcd(gcd(a, b), c)