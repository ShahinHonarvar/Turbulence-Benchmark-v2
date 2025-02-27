def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    x = nums[15]
    y = nums[51]
    z = nums[76]
    return gcd(gcd(x, y), z)