def gcf_two_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(nums[84], nums[13])