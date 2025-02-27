def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 86:
        raise ValueError('List must contain at least 86 elements')
    return gcd(gcd(nums[36], nums[85]), nums[83])