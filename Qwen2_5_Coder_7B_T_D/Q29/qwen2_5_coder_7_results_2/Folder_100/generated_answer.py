def gcf_two_nums(nums):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    return gcd(nums[96], nums[32])