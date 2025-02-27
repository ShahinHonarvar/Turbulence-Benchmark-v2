def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 13 and len(nums) > 54:
        return gcd(nums[54], nums[13])
    else:
        raise IndexError('The list must contain at least 55 elements.')