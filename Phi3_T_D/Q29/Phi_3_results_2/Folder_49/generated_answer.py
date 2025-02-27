def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 28:
        return gcd(nums[28], nums[20])
    else:
        raise IndexError('List does not have 29 or more elements.')