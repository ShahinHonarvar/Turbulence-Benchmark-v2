def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) > 94 and len(nums) > 57:
        return gcd(gcd(nums[93], nums[94]), nums[57])
    else:
        raise IndexError('The list is too short to access the specified indices.')