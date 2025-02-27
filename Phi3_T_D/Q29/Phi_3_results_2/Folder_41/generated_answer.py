def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 28:
        raise ValueError('List must contain at least 28 integers')
    return gcd(nums[23], nums[27])