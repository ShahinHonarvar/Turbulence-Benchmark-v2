def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1 = nums[912]
    n2 = nums[170]
    n3 = nums[500]
    return gcd(gcd(n1, n2), n3)