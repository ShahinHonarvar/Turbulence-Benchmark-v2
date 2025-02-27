def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 5:
        raise ValueError('The list must contain at least 5 integers.')
    return gcd(nums[4], nums[0])