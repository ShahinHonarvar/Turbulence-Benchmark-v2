def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    try:
        return gcd(nums[15], nums[99])
    except IndexError:
        raise ValueError('List should contain at least 100 elements.')