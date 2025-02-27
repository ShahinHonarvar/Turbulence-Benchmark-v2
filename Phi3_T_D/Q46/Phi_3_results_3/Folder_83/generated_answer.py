def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 57:
        raise ValueError('List must have at least 57 elements')
    return gcd(gcd(nums[56], nums[54]), nums[13])