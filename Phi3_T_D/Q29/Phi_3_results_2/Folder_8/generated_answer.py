def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[69] if 69 < len(nums) else 1, nums[41] if 41 < len(nums) else 1)