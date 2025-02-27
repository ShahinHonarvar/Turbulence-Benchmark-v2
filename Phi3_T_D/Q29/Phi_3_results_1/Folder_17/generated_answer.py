def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[69] if len(nums) > 69 else 0, nums[40] if len(nums) > 40 else 0)