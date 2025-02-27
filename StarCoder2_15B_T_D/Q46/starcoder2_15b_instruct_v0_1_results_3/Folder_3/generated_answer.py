def gcf_three_nums(nums):
    a = nums[31]
    b = nums[69]
    c = nums[40]

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)