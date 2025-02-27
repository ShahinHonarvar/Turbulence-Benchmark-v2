def gcf_two_nums(nums):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    return gcd(nums[64], nums[80]) if len(nums) > 80 else None