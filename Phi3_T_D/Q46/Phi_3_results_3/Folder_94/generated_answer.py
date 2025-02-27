def gcf_three_nums(nums):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(gcd(nums[56], nums[88]), nums[51])