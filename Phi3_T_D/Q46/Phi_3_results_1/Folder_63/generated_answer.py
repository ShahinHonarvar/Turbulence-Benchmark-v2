def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(nums[38], nums[52]), nums[69])