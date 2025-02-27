def gcf_three_nums(nums):

    def gcd(n1, n2):
        while n2:
            n1, n2 = (n2, n1 % n2)
        return n1
    return gcd(gcd(nums[4], nums[0]), nums[8])