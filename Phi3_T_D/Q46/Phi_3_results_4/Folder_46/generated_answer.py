def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 14:
        raise ValueError('List must have at least 14 elements.')
    return gcd(gcd(nums[78], nums[19]), nums[13])