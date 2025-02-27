def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 49 or len(nums) < 31:
        raise ValueError('List must contain at least 49 elements.')
    return gcd(nums[49], nums[31])