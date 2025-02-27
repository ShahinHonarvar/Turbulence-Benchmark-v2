def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < max(47, 97):
        return None
    return gcd(nums[47], nums[97])