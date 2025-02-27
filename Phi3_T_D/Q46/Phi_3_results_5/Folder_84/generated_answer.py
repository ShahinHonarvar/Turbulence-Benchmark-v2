def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[695] if 695 < len(nums) else 1, gcd(nums[710] if 710 < len(nums) else 1, nums[914] if 914 < len(nums) else 1))