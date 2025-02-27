def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    x = nums[20]
    y = nums[17]
    z = nums[28]
    return gcd(gcd(x, y), z)