def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[78] if 78 < len(nums) else 0, nums[93] if 93 < len(nums) else 0)