def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (nums[70], nums[41], nums[20])
    return gcd(gcd(a, b), c)