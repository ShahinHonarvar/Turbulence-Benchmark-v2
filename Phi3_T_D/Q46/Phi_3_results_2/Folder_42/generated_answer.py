def gcf_three_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(nums) < 97:
        raise ValueError('List must have at least 97 elements')
    return gcd(gcd(nums[19], nums[69]), nums[97])