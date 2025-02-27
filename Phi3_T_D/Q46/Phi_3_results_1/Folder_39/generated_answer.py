def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) >= 86:
        return gcd(gcd(nums[85], nums[35]), nums[53])
    else:
        return None