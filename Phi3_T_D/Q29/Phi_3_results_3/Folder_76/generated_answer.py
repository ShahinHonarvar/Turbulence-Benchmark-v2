def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_184 = nums[184]
    index_307 = nums[307]
    return gcd(index_184, index_307)