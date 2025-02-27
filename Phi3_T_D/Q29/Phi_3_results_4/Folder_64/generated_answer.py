def gcf_two_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(nums) < 10:
        return None
    return gcd(nums[6], nums[9])