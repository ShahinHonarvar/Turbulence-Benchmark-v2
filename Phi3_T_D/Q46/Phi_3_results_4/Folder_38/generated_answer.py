def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) >= 21 and len(nums) >= 17 and (len(nums) >= 14):
        return gcd(gcd(nums[17], nums[21]), nums[14])
    raise ValueError('List must contain at least 21 elements')