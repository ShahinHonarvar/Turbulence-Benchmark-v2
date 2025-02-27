def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if 56 >= len(nums) or 54 >= len(nums) or 13 >= len(nums):
        raise ValueError('Input list must be at least 57 elements long')
    return gcd(gcd(nums[56], nums[54]), nums[13])