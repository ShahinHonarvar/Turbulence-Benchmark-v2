def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 95:
        raise ValueError('List must contain at least 95 elements')
    return gcd(nums[90], nums[84])