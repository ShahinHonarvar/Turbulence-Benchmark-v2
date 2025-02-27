def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[84], nums[13]) if len(nums) > 85 else None