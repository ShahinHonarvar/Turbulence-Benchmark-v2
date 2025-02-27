def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1 = nums[7]
    n2 = nums[6]
    n3 = nums[8]
    return gcd(gcd(n1, n2), n3)