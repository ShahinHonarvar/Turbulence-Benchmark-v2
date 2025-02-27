def gcf_two_nums(nums):

    def gcd(a, b):
        return a if not b else gcd(b, a % b)
    return gcd(nums[49], nums[31])