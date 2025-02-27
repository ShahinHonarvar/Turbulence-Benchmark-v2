def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 56:
        raise ValueError('List does not have enough elements.')
    return gcd(nums[56], nums[54])